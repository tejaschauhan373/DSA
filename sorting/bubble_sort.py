def bubble_sort(input_list: list):
    """
    input_list: array of numbers
    Time Complexity :
    Best - Case : O(1)
    Average Case : O(n^2)
    Worst Case : O(n^2)
    """

    for i in range(len(input_list)):
        flag = 0
        for j in range(len(input_list) - 1 - i):
            if input_list[j] > input_list[j + 1]:
                input_list[j], input_list[j + 1] = input_list[j + 1], input_list[j]
                flag = 1

        if flag == 0:
            break
    return input_list


print(bubble_sort([12, 3, 4, 5, 6, 99, 1]))
print(bubble_sort([12, 3, 34, 5, 86, 99, 1]))
print(bubble_sort([1, 2, 3, 4, 5, 6]))
