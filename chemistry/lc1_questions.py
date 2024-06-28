import random
from questions_helpers import randomize_options, make_question

def q1(ran_num):
    vars = ["sodium", "potassium", "lithium", "calcium"]
    var = vars[ran_num % 4]
    question = '1. "' + str(var).capitalize() + ' metal is dissolved in deionized water to produce ' + str(var) + ' hydroxide solution and hydrogen gas". It is:'
    res = make_question('q1', question, "Chemical Change", ["Chemical Change", "Physical Change"])
    return res

def q2(ran_num):
    res = make_question('q2', '2. Carbon dioxide and carbon monoxide are mixed in a vessel. Is it an element, a compound, or a mixture?', 'Mixture', ['Element', 'Compound', 'Mixture'])
    return res

def q3(ran_num):
    vars = ["potassium", "carbon", "copper", "magnesium"]
    var = vars[ran_num % len(vars)]
    question = '3. Is ' + var + ' an element, a compound, or a mixture?'
    res = make_question('q3', question, 'Element', ['Element', 'Compound', 'Mixture'])
    return res

def q4(ran_num):
    res = make_question('q4', '4. "The normal melting point of water is 0 degrees Celsius". It is:', 'Physical Property', ['Chemical Property', 'Physical Property'])
    return res

def q5(ran_num):
    vars = ["potassium", "sodium", "lithium"]
    var = vars[ran_num % len(vars)]
    question = '5. "' + var.capitalize() + ' metal can react with water". It is:'
    res = make_question('q5', question, 'Chemical Property', ['Chemical Property', 'Physical Property'])
    return res

def q6(ran_num):
    vars1 = ["potassium", "sodium", "lithium"]
    var1 = vars1[ran_num % len(vars1)]
    vars2 = ["chloride", "bromide"]
    var2 = vars2[ran_num % len(vars2)]
    question = '6. "' + var1.capitalize() + ' ' + var2 + ' is dissolved in deionized water to produce ' + var1 + ' ' + var2 + 'aqueous solution". It is:'
    res = make_question('q6', question, 'Chemical Change', ['Chemical Change', 'Physical Change'])
    return res

def q7(ran_num):
    question = '7. Is carbon dioxide an element, a compound, or a mixture?'
    res = make_question('q7', question, 'Compound', ['Element', 'Compound', 'Mixture'])
    return res

def q8(ran_num):
    res = make_question('q8', '8. Sodium chloride is completely dissolved in deionized water to produce the sodium chloride aqueous solution. This solution is:', 'Homogeneous Mixture', ['Homogeneous Mixture', 'Heterogeneous Mixture'])
    return res

def q9(ran_num):
    question = '9. Sodium chloride is partly dissolved in deionized water to produce the sodium chloride aqueous solution with some remaining solid sodium chloride. This mixture is:'
    res = make_question('q9', question, 'Heterogeneous Mixture', ['Homogeneous Mixture', 'Heterogeneous Mixture'])
    return res

def q10(ran_num):
    res = make_question()
    return res

def learning_check_1(username):
    seed = (int(username[4:6]) * 100) + int(username[7:])
    random.seed(seed)
    questions = []
    ran_num = int(random.random() * 1000000)
    questions.append(q1(ran_num))
    questions.append(q2(ran_num))
    questions.append(q3(ran_num))
    questions.append(q4(ran_num))
    questions.append(q5(ran_num))
    questions.append(q6(ran_num))
    questions.append(q7(ran_num))
    questions.append(q8(ran_num))
    questions.append(q9(ran_num))
    return questions

