
# Insertion sort is iteratively inserting an element into its correct position within a sorted section of the list.

def insertionSort(array):
    for x in range(1, len(array)):
        elem = array[x]

        y = x - 1

        while y >= 0 and elem < array[y]:
            array[y + 1] = array[y]
            y = y - 1

        array[y + 1] = elem

    return array