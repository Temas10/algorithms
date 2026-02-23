def heapify(arr, n, i):
    largest = i          # Инициализируем наибольший элемент как корень
    left = 2 * i + 1      # левый дочерний элемент
    right = 2 * i + 2     # правый дочерний элемент

    # Проверяем, больше ли левый дочерний элемент корня
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Проверяем, больше ли правый дочерний элемент корня
    if right < n and arr[right] > arr[largest]:
        largest = right

    # Если наибольший элемент не корень
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Обмен

        # Рекурсивно приводим к свойствам кучи поддерево
        heapify(arr, n, largest)

def heap_sort_manual(arr):
    n = len(arr)

    # Построение max-heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Извлечение элементов из кучи
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # Обмен
        heapify(arr, i, 0)

    return arr

example = [12, 11, 13, 5, 6, 7]
print(heap_sort_manual(example))  # [5, 6, 7, 11, 12, 13]