# https://unstop.com/practice/company-preparation/deloitte/deloitte-coding-assessment-29641/question-29697
import sys

def removeDuplicates(s: str) -> str:
    stack = []
    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
    return "".join(stack)

try:
    input_string = sys.stdin.readline().strip() 
except:
    input_string = ""

if input_string:
    result = removeDuplicates(input_string)
    print(result)
