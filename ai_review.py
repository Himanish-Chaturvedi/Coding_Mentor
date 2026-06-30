import enigne

def review_code():

    with open("problems/problem1/statement.txt", "r") as f:
        question = f.read()

    with open("submissions/solution.py", "r") as f:
        code = f.read()

    response = enigne.ai_review(question, code)

    return response

