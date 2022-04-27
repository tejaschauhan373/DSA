keypad = {0: "",
          1: "",
          2: "ABC",
          3: "DEF",
          4: "GHI",
          5: "JKL",
          6: "MNO",
          7: "PQRS",
          8: "TUV",
          9: "WXYZ"}


def print_keypad_output(input_str: str, output_str: str, i: int = 0):
    if i == len(input_str):
        print(output_str)
        return

    current_digit = int(input_str[i])

    if current_digit == 0 and current_digit == 1:
        print_keypad_output(input_str, output_str, i + 1)

    for character in keypad[current_digit]:
        print_keypad_output(input_str, output_str + character, i + 1)
    return


n = "234"

print_keypad_output(n, "", 0)
