import time

# Implementacion of Quicksort algorithm.

# The function takes the last element as pivot (not necessary to take always the last element)
# places the element at its correct position sorted array and places all smaller elements
# (smaller than pivot) to the left of pivot and all greater element to the right of pivot.

def Partition(array, low, high):
    index = (low - 1)   # Index of the smaller ellement
    pivot = array[high] # Pivot

    for iter in range(low, high):
        # If current element is smallet than or equal to pivot (Never can be greater than pivot).
        if array[iter] <= pivot:
            # Increment index of the smaller element.
            index = index + 1
            array[index], array[iter] = array[iter], array[index]

    array[index + 1], array[high] = array[high], array[index + 1]
    return(index + 1)


# The main function that implements Quicksort
#   Array -> The array to be sorted
#   Low -> The starting index
#   High -> The ending index

def Quicksort(array, low, high):
    if len(array) == 1:
        return array
    if low < high:
        # Pivot is partitioning index
        pivot = Partition(array, low, high)

        # Separately sort elements before partition and after partition
        Quicksort(array, low, pivot-1)
        Quicksort(array, pivot+1, high)


# Driver code to test sort
ARRAY = [10, 7, 8, 1, 4, 9, 2, 5, 3, 6]
N = len(ARRAY)

Quicksort(ARRAY, 0, N-1)
print("Sorted array is: ", ARRAY)