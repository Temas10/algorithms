def shell_sort(arr):
    n = len(arr)
    # Начинаем с большого промежутка, затем уменьшаем его
    gap = n // 2

    while gap > 0:
        # Выполняем сортировку вставками с текущим промежутком
        for i in range(gap, n):
            temp = arr[i]
            j = i

            # Сдвигаем элементы, которые больше temp и находятся на gap позиций левее
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap

            arr[j] = temp

        gap //= 2

    return arr

example = [12, 34, 54, 2, 3]
print(shell_sort(example))  # [2, 3, 12, 34, 54]