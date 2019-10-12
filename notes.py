# Merge sort:
#  - Review, solution
#  - Divide and Conquer

# Timing comparisons
#  - Compare timing of various sorts
#  - Practical timing benchmarks
#  - Plotting big-O curves

# Recursion Review
#  - Dynamic Programming, Caching

# More Polya Practice
#  - Taking a first pass at a solution with N-fibonacci
#  - Improving on your N-fib with dynamic programming
#  - Improve on some previous first pass solutions

# complexity is how fast your code runs
import random
items = [1, 54, 6, 6, 3,32, 34, 6]
def quicksort(items):
    if len(items) <= 1:
        return items
    # 1. Select the last element as the pivot.
    pivot = items[-1]
    left = []
    right = []
    for i in range(len(items) - 1):
        item = items[i]
        if item < pivot:
            # 2. Move all elements smaller than the pivot to the left.
            left.append(item)
        else:
            # 3. Move all elements greater than the pivot to the right.
            right.append(item)
    # 4. While LHS and RHS are greater than 1, repeat steps 1-3 on each side.
    return quicksort(left) + [pivot] + quicksort(right)

def insertion_sort(items):
    # Split the list into sorted and unsorted
    # For each element in unsorted...
    counter = 0
    for i in range(1, len(items)):
        # print(items)
        # Insert that element into the correct place in sorted by:
        # Store the element in a temp variable
        temp = items[i]
        # Shifting all larger sorted elements to the right by 1
        j = i
        while j > 0 and temp < items[j - 1]:
            counter += 1
            items[j] = items[j - 1]
            j -= 1
        # Insert the element after the first smaller elememnt
        items[j] = temp
        # print(f"counter: {counter}")
    return items


l = [2, 4, 3, 0, 1, 5, 8, 7, 9, 6]
random.shuffle(l)
# insertion_sort(l)



def bubble_sort(items):
    has_swapped = False
    for i in range(len(items) - 1):
        # Compare each element to its neighbor
        # If elements in wrong position relative to each other
        if items[i] > items[i+1]:
            # swap them
            items[i], items[i+1] = items[i+1], items[i]
            has_swapped = True
    if has_swapped:
        return bubble_sort(items)
    else:
        return items





def merge(arrA, arrB):
    '''
    Take 2 sorted arrays and merge them into a single
    sorted array containing all elements from both
    '''
    # Create a new, array of length len(arrA) + len(arrB)
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # Create markers for a and b starting at 0
    a = 0
    b = 0
    # While a and b are less than the length of the arrA and arrB respectively
    for i in range(0, elements):
        # Compare the items at indices a/b, add the smallest to the merged array
        # Increment a/b, whichever was smallest
        if a >= len(arrA):
            merged_arr[i] = arrB[b]
            b += 1
        elif b >= len(arrB):
            merged_arr[i] = arrA[a]
            a += 1
        elif arrA[a] < arrB[b]:
            merged_arr[i] = arrA[a]
            a += 1
        else:  # arrA[a] >= arrB[b]
            merged_arr[i] = arrB[b]
            b += 1
    return merged_arr


def merge_sort(arr):
    '''
    Take an unsorted list, return a sorted list
    '''
    if len(arr) <= 1:
        return arr
    else:
        # Split this in half
        left_half = arr[0 : len(arr) // 2]
        right_half = arr[len(arr) // 2 : ]
        # Sort the halves
        left_sorted = merge_sort(left_half)
        right_sorted = merge_sort(right_half)
        # Merge the sorted halves
        return merge(left_sorted, right_sorted)


list = [2, 4, 3, 0, 1, 5, 8, 7, 9, 6]
merge_sort(list)





from time import time

l = [random.randint(0, 1000) for i in range(0, 100000)]


lists = []
for i in range(1, 10):
    l = [random.randint(0, 1000) for i in range(0, i * 1000)]
    lists.append(l)


# start_time = time()
# # Run our code
# quicksort(l)
# # Store the ending time
# end_time = time()
# print (f"{end_time - start_time} seconds")
#
# ​​
insertion_sort_times = {}
for l in lists:
    start_time = time()
    # Run our code
    insertion_sort(l)
    # Store the ending time
    end_time = time()
    insertion_sort_times[len(l)] = end_time - start_time

print(insertion_sort_times)



for key in insertion_sort_times:
    print(insertion_sort_times[key])