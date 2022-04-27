# Print all possible  permutation of given string

def print_permutation(array_of_characters: list, index: int):
    if index == len(array_of_characters) - 1:
        print("".join(arr))

    for j in range(index, len(array_of_characters)):
        new_arr = array_of_characters.copy()
        new_arr[index], new_arr[j] = new_arr[j], new_arr[index]
        print_permutation(new_arr, index + 1)


arr = []
s = "ABCD"

for i in s:
    arr.append(i)
print(print_permutation(arr, 0))
