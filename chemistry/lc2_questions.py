import random
from questions_helpers import randomize_options, make_question

def q1(ran_num):
    vars = ["sodium", "potassium", "lithium", "calcium"]
    var = vars[ran_num % 4]
    question = '1. "' + str(var).capitalize() + ' metal is dissolved in deionized water to produce ' + str(var) + ' hydroxide solution and hydrogen gas". It is:'
    res = make_question(1, question, "Chemical Change", ["Chemical Change", "Physical Change"])
    return res

def learning_check_2(username):
    seed = (int(username[4:6]) * 100) + int(username[7:])
    random.seed(seed)
    questions = []
    ran_num = int(random.random() * 1000000)
    """
    questions.append(q1(ran_num))
    questions.append(q2(ran_num))
    questions.append(q3(ran_num))
    questions.append(q4(ran_num))
    questions.append(q5(ran_num))
    questions.append(q6(ran_num))
    questions.append(q7(ran_num))
    questions.append(q8(ran_num))
    questions.append(q9(ran_num))
    """
    return questions
