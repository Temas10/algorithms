def heap_sort(arr):
    import heapq

    # Преобразуем исходный массив в кучу
    heap = arr.copy()
    heapq.heapify(heap)

    # Извлекаем элементы из кучи в отсортированном порядке
    sorted_array = []
    while heap:
        sorted_array.append(heapq.heappop(heap))

    return sorted_array

example = [12, 11, 13, 5, 6, 7]
print(heap_sort(example))  # [5, 6, 7, 11, 12, 13]