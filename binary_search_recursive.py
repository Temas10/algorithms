def binary_search_recursive(arr, target, left=0, right=None):
    if right is None:
        right = len(arr) - 1

    # Базовый случай: элемент не найден
    if left > right:
        return -1

    mid = (left + right) // 2

    # Если элемент найден
    if arr[mid] == target:
        return mid

    # Рекурсивный случай: ищем в левой половине
    elif arr[mid] > target:
        return binary_search_recursive(arr, target, left, mid - 1)

    # Рекурсивный случай: ищем в правой половине
    else:
        return binary_search_recursive(arr, target, mid + 1, right)


sorted_example = [7, 9, 20, 4, 11, 64, 71]
target = 11
result = binary_search_recursive(sorted_example, target)
print(f"Элемент {target} найден на позиции {result}" if result != -1 else f"Элемент {target} не найден")