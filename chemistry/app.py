import os
import re
from lc1_questions import learning_check_1

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, send_from_directory, url_for
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash
from time import gmtime, strftime
from math import ceil


from helpers import apology, login_required, check_password

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

db = SQL("sqlite:///chemistry.db")

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/") #TODO:front-end
@login_required
def index():
    id = session["user_id"]
    return render_template("index.html")


@app.route("/test_lc", methods=["GET", "POST"]) #TODO:front-end
@login_required
def test_lc():
    id = session["user_id"]
    username = db.execute("SELECT username FROM users WHERE id = ?", id)[0]["username"]
    x = int(username[4:6])
    y = int(username[7:]) + 7
    ans = x + y
    option2 = x + y + 3
    option3 = 2 * (x + y)
    if request.method == "POST":
        if int(request.form.get("options")) == ans:
            return render("correct.html")
        else:
            return redirect("/")

    elif request.method == "GET":
        #Get username (student id)
        question = "What is {x} + {y}".format(x = x, y = y) #put in helpers

        return render_template("test_lc.html", question=question, ans=ans, option2=option2, option3=option3)

@app.route("/lc1", methods=["GET", "POST"]) #TODO:front-end
@login_required
def lc1_questions():
    id = session["user_id"]
    lc_num = 1
    username = db.execute("SELECT username FROM users WHERE id = ?", id)[0]["username"]
    questions = learning_check_1(username)
    questions_num = len(questions)

    if request.method == 'GET':
        if db.execute('SELECT * FROM lc_submission WHERE lc_num = ? AND student_id = ?', lc_num, username):
            score = db.execute('SELECT score FROM lc_scores WHERE lc_num = ? AND student_id = ?', lc_num, username)[0]['score']
            submission = db.execute('SELECT * FROM lc_submission WHERE lc_num = ? AND student_id = ?', lc_num, username)[0]
            #TODO
            return render_template('lc1_done.html', questions=questions, submission=submission, score=score)
        return render_template("lc1.html", questions=questions)

    elif request.method == 'POST':
        clause = '(lc_num,student_id,'
        placeholders = '(?,?,'
        values = [lc_num, username]
        score = 0
        for question in questions:
            clause += question['number'] + ','
            placeholders += '?,'
            if request.form.get(question['number']) == question['answer']:
                score += 1
            values.append(request.form.get(question['number']))
        score = score * 100.0 / len(questions)
        clause = clause[:-1] + ')'
        placeholders = placeholders[:-1] + ')'
        query = 'INSERT INTO lc_submission ' + clause + ' VALUES' + placeholders
        db.execute(query, *values)
        db.execute('INSERT INTO lc_scores (lc_num, student_id, score) VALUES (?, ?, ?)', lc_num, username, score)
        return redirect('/lc1')


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    # /register reached via POST
    if request.method == "POST":
        usernames = db.execute("SELECT username FROM users")
        usernames = [row["username"] for row in usernames]

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 400)

        # Ensure username does not exist
        elif request.form.get("username") in usernames:
            return apology("username already exists", 400)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 400)

        # Ensure password match password confirmation
        elif request.form.get("password") != request.form.get("confirmation"):
            return apology("password does not match password confirmation", 400)

        elif request.form.get("username") in usernames:
            return apology("username already exists", 400)

        username = request.form.get("username")
        rex = re.compile("^[B]{1}[0-9]{8}$")
        password = request.form.get("password")
        if not rex.match(username):
            return apology("wrong username format (B1XXXXXXX)", 400)
        elif not check_password(password):
            return apology("password must be at least 8 characters long and contain at least 1 letter and 1 number", 400)

        # Add username and hash into db
        hash = generate_password_hash(request.form.get("password"), method='pbkdf2:sha256', salt_length=8)
        db.execute("INSERT INTO users (username, hash) VALUES(?, ?)", request.form.get("username"), hash)
        return redirect("/login")

    # /register reached via GET
    else:
        return render_template("register.html")


@app.route("/login", methods=["GET", "POST"]) #DONE
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")

@app.route("/logout") #DONE
def logout():
    session.clear()
    return redirect("/")

@app.route("/changepassword", methods=["GET", "POST"]) #DONE
@login_required
def changepassword():
    id = session["user_id"]
    if request.method == "POST":
        old_password = request.form.get("old_password")
        old_password_hash = db.execute("SELECT hash FROM users WHERE id = ?", id)
        if not check_password_hash(old_password_hash, old_password):
            return apology("old password incorrect", 400)
        new_password = request.form.get("new_password")
        new_password_hash = generate_password_hash(new_password, method='pbkdf2:sha256', salt_length=8)
        db.execute("UPDATE users SET hash = ? WHERE id = ?", new_password_hash, id)
        return redirect("/logout")

    elif request.method == "GET":
        return render_template("changepassword.html")
"""
@app.route("/lc1") #TODO:front-end
@login_required
def index():
    #Set status to done and prevent taking again
    id = session["user_id"]
    return render_template("lc1.html")
"""
