string = "((())[]{})"

def validParentheses(string):
    opposite_parentheses = {')':'(','}':'{',']':'['}
    stack = []
    for i in string:
        if i in opposite_parentheses:
            if stack and stack[-1]==opposite_parentheses[i]:
                stack.pop()
            else: stack.append(i)
        else: stack.append(i)
    if stack:
        return False
    return True

print(validParentheses(string))