
# Insertion sort is iteratively inserting an element into its correct position within a sorted section of the list.

def insertionSort(array):
    arrayLength = len(array)

    if arrayLength <= 1:
        return array

    for x in range(1, arrayLength):
        elem = array[x]

        y = x - 1

        while y >= 0 and elem < array[y]:
            array[y + 1] = array[y]
            y = y - 1

        array[y + 1] = elem

    return array

# Array to be sorted
array = [6, 2, 3, 5, 7, 9, 1, 8]
print("array to be sorted: " + str(array))
# Print array
print("sorted array: " + str(insertionSort(array)))

# Test case of 1 or less elements in array for insertion sort
newArray = [3]
print("new array with one or less element to be sorted: " + str(newArray))
# Print array
print("new array sorted: " + str(insertionSort(newArray)))