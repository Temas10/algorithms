def bubble_sort(arr):
    b = len(arr)
    for i in range(b):
        flag = False
        for j in range(0, b - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                flag = True
        if not flag:
            break
    return arr

example = [45, 25, 44, 11, 5, 120, 4]
print(bubble_sort(example))  # [4, 5, 11, 25, 44, 45, 120]