array_to_sort = [5, 2, 6, 8, 9, 1, 7, 16, 22, 18, 12]

def selection_sort(arr):
    array_length = len(arr)
    array = arr

    for i in range(array_length - 1):
        current_smallest_int_index = 1
        
        for j in range(i + 1, array_length):
            if array[current_smallest_int_index] > array[j]:
                current_smallest_int_index = j

        array[i], array[current_smallest_int_index] = (array[current_smallest_int_index], array[i])
    return array

selection_sort(array_to_sort)
print(array_to_sort)