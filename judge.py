import subprocess

def judge_submission():
    input_file = "problems/problem1/input.txt"
    expected_file = "problems/problem1/expected_output.txt"
    solution_file = "submissions/solution.py"

    with open(input_file, "r") as f:
        test_input = f.read()

    with open(expected_file, "r") as f:
        expected_output = f.read().strip()

    try:
        result = subprocess.run(
            ["python", solution_file],
            input=test_input,
            text=True,
            capture_output=True,
            timeout=5
        )

        if result.returncode != 0:
            print("Runtime Error")
            print(result.stderr)
            return

        actual_output = result.stdout.strip()

        if actual_output == expected_output:
            print("Passed")
        else:
            print("Failed")
            print("Expected:", expected_output)
            print("Got:", actual_output)

    except subprocess.TimeoutExpired:
        print("Time Limit Exceeded")