from random import sample

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

print('---------------------------------------------------------------------------------------')
print('B I N A R Y                   S E A R C H                   I M P L E M E N T A T I O N')
print('---------------------------------------------------------------------------------------\n\n')

sample_size = int(input('Enter the size of random sized sorted array ::  '))

sample_array = sorted(sample(range(1, 1000), sample_size))
print(f"\nSample random array is {sample_array}\n")

element_to_be_searched = int(input('Enter a number to be searched :: '))

print('\n\n               >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>               ')
print('               B I N A R Y           S E A R C H           R E S U L T S               ')
print('               <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<               ')

searched_index = binary_search(sample_array, element_to_be_searched, 0, len(sample_array) - 1)

print(f'\n\n               In the selected list element {element_to_be_searched} is {"not present" if searched_index == -1 else f"present at index {searched_index}"}', end="")

print('\n\n\n---------------------------------------------------------------------------------------')
print('B I N A R Y                   S E A R C H                   I M P L E M E N T A T I O N')
print('---------------------------------------------------------------------------------------\n\n\n')