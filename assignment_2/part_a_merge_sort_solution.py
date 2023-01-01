



def merge_sort(array):
    if len(array) > 1:
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]

        merge_sort(left)
        merge_sort(right)
        
        array = merge_arrays(array, left, right)
        
    return array

def merge_arrays(array, left, right):
    x = y = z = 0
    
    while x < len(left) and y < len(right):
        if left[x] < right[y]:
            array[z] = left[x]
            x += 1
            z += 1
        else:
            array[z] = right[y]
            y += 1
            z += 1
    
    while y < len(right):
        array[z] = right[y]
        y += 1
        z += 1

    while x < len(left):
        array[z] = left[x]
        x += 1
        z += 1
    
    return array

A = [11, -8, 10, 1, -12, 15, -17, 5, -13, -20, 16, 7, -3, 18, -7, -15, 13, 6, 4, -9]

sorted_array = merge_sort(A)

print(f"Sorted array {sorted_array}")