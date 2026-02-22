def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        # Рекурсивная сортировка подмассивов
        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        # Слияние подмассивов
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        # Проверка оставшихся элементов
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

    return arr

numbers = [56, 66, 4, 2, 224, 15, 80]
print(merge_sort(numbers))  # [2, 4, 15, 56, 66, 80, 224]