import random
import time

# Insertion sort code:
def insertion_sort(A):
    N = len(A)
    for j in range(1, N):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i + 1] = A[i]
            i -= 1
        A[i + 1] = key
    return A

# Quicksort code:
def quicksort(my_list, cutoff):
    if len(my_list) <= cutoff:
        return insertion_sort(my_list)
    else:
        pivot = my_list[0]
        end_of_smaller_than_block = 0

        for end_of_larger_than_block in range(0, len(my_list) - 1):

            if my_list[end_of_larger_than_block + 1] < pivot:

                my_list[end_of_larger_than_block + 1], my_list[end_of_smaller_than_block + 1] = (
                my_list[end_of_smaller_than_block + 1],
                my_list[end_of_larger_than_block + 1],)
                end_of_smaller_than_block += 1

        my_list[0], my_list[end_of_smaller_than_block] = my_list[end_of_smaller_than_block], my_list[0]


        first_part = quicksort(my_list[:end_of_smaller_than_block], cutoff)
        second_part = quicksort(my_list[end_of_smaller_than_block + 1:], cutoff)
        first_part.append(my_list[end_of_smaller_than_block])
        return first_part + second_part


# Driver code
cutoffs = [10, 25, 50, 75, 100]
for cutoff in cutoffs:
    my_list = list(range(1000000))
    random.shuffle(my_list)

    start_time = time.time()
    sorted_list = quicksort(my_list, cutoff=cutoff)
    end_time = time.time()
    time_taken = end_time - start_time

    print(sorted_list[:10])
    print(f"Cutoff: {cutoff} | Time: {time_taken:.4f} seconds")
