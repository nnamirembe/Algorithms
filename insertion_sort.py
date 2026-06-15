
import math
import random




def insert_sort(A):
	maximum_index = len(A)
	for j in range(1, maximum_index):
		key = A[j]
		i = j - 1
		while i >= 0 and A[i] > key:
			A[i + 1] = A[i]
			i -= 1
		A[i + 1] = key
	return(A)

my_list = list(range(0,100000))

random.shuffle(my_list)
sorted_list = insert_sort(my_list)
print(sorted_list)
