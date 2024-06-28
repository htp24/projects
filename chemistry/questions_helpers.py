import random

"""
((question, answer, A, B, C, D), ...)
question = {
    question: ...,
    answer: ...,
    options: []
}
"""

def randomize_options(ran_num):
    random.Random(ran_num).shuffle(options)
    return options

def make_question(number, question, ans, options):
    res = {
        "number": number,
        "question": question,
        "answer": ans,
        "options": options
    }
    return res
