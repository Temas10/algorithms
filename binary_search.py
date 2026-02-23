def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        # Если элемент найден
        if arr[mid] == target:
            return mid

        # Если элемент меньше среднего, ищем в левой половине
        elif arr[mid] > target:
            right = mid - 1

        # Если элемент больше среднего, ищем в правой половине
        else:
            left = mid + 1

    return -1  # Элемент не найден


sorted_example = [11, 12, 22, 25, 34, 64, 90]
target = 25
result = binary_search(sorted_example, target)
print(f"Элемент {target} найден на позиции {result}" if result != -1 else f"Элемент {target} не найден")