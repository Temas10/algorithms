def radix_sort(arr):
    # Находим максимальное число для определения количества цифр
    max_num = max(arr)

    # Выполняем сортировку подсчетом для каждого разряда
    exp = 1
    while max_num // exp > 0:
        counting_sort_by_digit(arr, exp)
        exp *= 10

    return arr

def counting_sort_by_digit(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    # Подсчитываем количество каждой цифры
    for i in range(n):
        digit = (arr[i] // exp) % 10
        count[digit] += 1

    # Накапливаем суммы для определения позиций
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Создаем отсортированный по текущему разряду массив
    for i in range(n - 1, -1, -1):
        digit = (arr[i] // exp) % 10
        output[count[digit] - 1] = arr[i]
        count[digit] -= 1

    # Копируем отсортированный массив обратно в исходный
    for i in range(n):
        arr[i] = output[i]

example = [170, 45, 75, 90, 802, 24, 2, 66]
print(radix_sort(example)) # [2, 24, 45, 66, 75, 90, 170, 802]