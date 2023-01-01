def binary_search(array, value, left, right):
    if right >= left:
        mid_index = (left + right) // 2

        if array[mid_index] == value:
            return mid_index
        
        elif array[mid_index] > value:
            return binary_search(array, value, left, mid_index - 1)

        else:
            return binary_search(array, value, left + 1, right)
    else:
        return -1

sample_array = [2, 6, 7, 9, 17, 27, 56, 78, 87, 98]

print(f"\nSample array is {sample_array}\n")

element_to_be_searched = int(input('Enter a number to be searched :: '))

searched_index = binary_search(sample_array, element_to_be_searched, 0, len(sample_array) - 1)

print(f'\nElement is {"not present" if searched_index == -1 else f"present at index {searched_index}"}')