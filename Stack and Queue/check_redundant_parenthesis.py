def is_there_redundant_parenthesis(expression: str):
    stack = []

    for char in expression:

        if char != ")":
            stack.append(char)
        else:
            found_operator = False
            while stack and stack[-1] != "(":
                if stack[-1] in {"+": 0, "-": 0, "*": 0, "/": 0}:
                    found_operator = True
                stack.pop()

            if found_operator and stack and stack[-1] == "(":
                stack.pop()
            else:
                return False

    return True


exp = "(((a+b)+c)+(c*d))"
print(is_there_redundant_parenthesis(exp))
