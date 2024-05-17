def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def binary_search(item, arr):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == item:
            return mid
        elif arr[mid] < item:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Пример использования функций
unsorted_list = [64, 34, 25, 12, 22, 11, 90]
print("Неотсортированный список:", unsorted_list)

# Применяем сортировку пузырьком
sorted_list = bubble_sort(unsorted_list.copy())
print("Отсортированный список (пузырьковая сортировка):", sorted_list)

# Применяем сортировку выбором
sorted_list_selection = selection_sort(unsorted_list.copy())
print("Отсортированный список (сортировка выбором):", sorted_list_selection)

# Применяем двоичный поиск
item_to_search = 25
index = binary_search(item_to_search, sorted_list)
if index != -1:
    print(f"Элемент {item_to_search} найден по индексу {index} в отсортированном списке.")
else:
    print(f"Элемент {item_to_search} не найден в отсортированном списке.")
