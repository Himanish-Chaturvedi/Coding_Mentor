

import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("api_key")

client = genai.Client(api_key=api_key)

def ai_review(question,code):
      prompt= f'''You are an expert Python interviewer and mentor.

 Programming Question:
 {question}

 Student's Python Code:
 {code}

 Analyze the submission and return:

 1. Is the solution correct?
 2. Explain the logic used.
 3. Time Complexity.
 4. Space Complexity.
 5. Coding mistakes (if any).
 6. Better approach (if applicable).
 7. Alternative ways to solve this problem.
 8. Pythonic improvements.
 9. Final Verdict (Correct / Incorrect / Partially Correct).

 Do not simply rewrite the entire code unless necessary.
 Explain like you're mentoring a student.'''
 
      response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt )
      return response.text

