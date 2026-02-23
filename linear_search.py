def linear_search(arr, target):
    for i, item in enumerate(arr):
        if item == target:
            return i 
    return -1 

# Пример использования
example = [4, 17, 25, 7, 10, 14, 89]
target = 10
result = linear_search(example, target)
print(f"Элемент {target} найден на позиции {result}" if result != -1 else f"Элемент {target} не найден")


# enumerate() — это встроенная функция, которая позволяет получить 
# при итерации не только элементы последовательности, но и их индексы. 
# Она возвращает специальный объект-итератор, генерирующий кортежи вида (индекс, элемент).
