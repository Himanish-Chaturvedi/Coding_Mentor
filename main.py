from executor import execute_code
from validator import validate_output
from ai_review import review_code

executed = execute_code()

if validate_output(executed):
    print("PASS")
else:
    print("FAIL")


review = review_code()

print(executed)
print(review)