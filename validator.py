def validate_output(actual_output):
    
    with open ("problems/problem1/expected_output.txt","r") as f:
        exp = f.read().strip()
        
    act = actual_output.strip()
        
    return act == exp
            