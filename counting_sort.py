def counting_sort(arr):
    # Находим максимальное и минимальное значение для создания массива подсчёта
    max_value = max(arr)
    min_value = min(arr)
    range_of_values = max_value - min_value + 1

    # Создаем массив подсчёта
    count = [0] * range_of_values

    # Подсчитываем количество каждого элемента
    for num in arr:
        count[num - min_value] += 1

    # Восстанавливаем отсортированный массив
    sorted_array = []
    for i in range(range_of_values):
        sorted_array.extend([i + min_value] * count[i])

    return sorted_array

example = [4, 2, 2, 8, 3, 3, 1]
print(counting_sort(example))  # [1, 2, 2, 3, 3, 4, 8]