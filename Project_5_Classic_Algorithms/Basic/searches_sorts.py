# Classic Search and Sort Algorithms

# Searches: Linear Search and Binary Search

def linear_search(values, target):
    """ Search a list and return the index if found.
    Returns -1 if target is not found.
    """

    for i in range(len(values)):
        if target == values[i]:
            return i
    
    return -1


def binary_search(values, target):   
    """ Search a list and return the index if found.
    Returns -1 if target is not found.
    """

    lower = 0
    upper = len(values) - 1

    while lower <= upper:
        mid = (lower + upper) // 2

        if target == values[mid]:
            return mid
        elif values[mid] > target:
            upper = mid - 1
        else:
            lower = mid + 1

    return -1

# Sorts: Bubble, Merge, Selection, and Insertion

def bubble_sort(unsorted_values):
    """ Sorts a list of unsorted values. """

    done = False
    sorted_count = 0

    while not done:
        done = True
        index = 0

        while index < len(unsorted_values) - 1 - sorted_count:
            if unsorted_values[index] > unsorted_values[index + 1]:
                swap(unsorted_values, index, index + 1)
                done = False
            index += 1
        sorted_count += 1

def insertion_sort(values):
    for i in range(1, len(values)):
        temp = values[i]
        j = i - 1
        while j >= 0 and values[j] > temp:
            values[j + 1] = values[j]
            j = j - 1
        values[j + 1] = temp
    
def selection_sort(values):
    for i in range(len(values)):
        best = i
        for j in range(i + 1, len(values)):
            if values[j] < values[best]:
                best = j
        swap(values, i, best)

def merge_sort(values):
    # Base Case: when the values is size 1 (sorted)
    if len(values) <= 1:
        return values

    # temp list that will hold our sorted values to return them later
    sorted_values = []

    # finding the mid so we can divide the list into lower and upper halves
    mid = len(values) // 2

    # Dividing the list in half and caling mergeSort again on each one
    # to further divide the list down into smaller halves
    # and then catching back the sorted smaller halves
    lower_half = merge_sort(values[:mid])
    upper_half = merge_sort(values[mid:])

    # Sorting the halves that were returned from above
    # Checking the first item of each and the lower is inserted into
    # sortedValues first.
    while len(lower_half) > 0 and len(upper_half) > 0:
        if lower_half[0] < upper_half[0]:
            sorted_values.append(lower_half.pop(0))
        else:
            sorted_values.append(upper_half.pop(0))

    # There might be some left over sorted values in each half
    # If there is, add them all (extend) to the end of sortedValues
    # since they must all be larger than what is already there.
    if len(lower_half) > 0:
        sorted_values.extend(lower_half)
    elif len(upper_half) > 0:
        sorted_values.extend(upper_half)   

    # Return the sorted values.
    return sorted_values     

# Helper Functions

def swap(values, i, j):
    """ Swap values[i] with values[j] inside of list values. """

    temp = values[i]
    values[i] = values[j]
    values[j] = temp