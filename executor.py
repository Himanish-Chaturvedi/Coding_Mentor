import subprocess

def execute_code():
    with open ("problems/problem1/input.txt","r") as f:
        code = f.read()
        
    result = subprocess.run (
        ["python","submissions/solution.py"],
        input=code,
        capture_output=True,
        text=True)
    
    return result.stdout
