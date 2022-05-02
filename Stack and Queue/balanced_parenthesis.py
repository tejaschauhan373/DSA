def is_balanced_parenthesis(expression: str) -> bool:
    stack = []

    for char in expression:
        if char == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                return False
        elif char == "]":
            if stack and stack[-1] == "[":
                stack.pop()
            else:
                return False
        elif char == "}":
            if stack and stack[-1] == "{":
                stack.pop()
            else:
                return False
        elif char in {"[": 0, "{": 0, "(": 0}:
            stack.append(char)

    return len(stack) == 0


exp = "(A+B*(C+B-D))"
print(is_balanced_parenthesis(exp))
