import random
import time

class Heapsort:

	def __init__(self):
		pass

	def Make_maxheap(self, my_list, list_size):
		for node_index in range(list_size - 1 // 2, -1, -1):
			self.Heapify(my_list, list_size, node_index)

	def Heapify(self, my_list, list_size, node_index):
		largest = node_index  # Initialize largest as root
		left_child = 2 * node_index + 1  # left = 2*node_index + 1
		right_child = 2 * node_index + 2  # right = 2*node_index + 2
		if left_child < list_size and my_list[node_index] < my_list[left_child]:
			largest = left_child
		if right_child < list_size and my_list[largest] < my_list[right_child]:
			largest = right_child
		if largest != node_index:
			my_list[node_index], my_list[largest] = my_list[largest], my_list[node_index]  # swap
			self.Heapify(my_list, list_size, largest)

	def Heap_unwind(self, my_list, list_size):
		# One by one extract elements
		for node_index in range(list_size - 1, 0, -1):
			my_list[node_index], my_list[0] = my_list[0], my_list[node_index]  # swap
			self.Heapify(my_list, node_index, 0)

	# The main function to sort an array of given size
	def Heapsort(self, my_list):
		list_size = len(my_list)
		# Build a maxheap.
		self.Make_maxheap(my_list, list_size)
		self.Heap_unwind(my_list, list_size)




# Driver code

heapsort = Heapsort()
my_list = list(range(0,1000000))
random.seed()
random.shuffle(my_list)
start = time.time()
heapsort.Heapsort(my_list)
end = time.time()
print(end-start)
#print(my_list)