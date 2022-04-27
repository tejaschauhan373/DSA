# Generate valid brackets using recursion

def generate_bracket_code(output: str, n: int, open: int, close: int, i: int):
    if i == 2 * n:
        print(output)
        return

    if open < n:
        generate_bracket_code(output + "(", n, open + 1, close, i + 1)

    if close < open:
        generate_bracket_code(output + ")", n, open, close + 1, i + 1)


n = 3
print(generate_bracket_code("", 3, 0, 0, 0))
