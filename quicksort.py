import random
import time

class Quicksort:

	def Quicksort(self, my_list):
		if len(my_list) <= 1:
			return my_list
		else:
			pivot = my_list[0]
			end_of_smaller_than_block = 0
			for end_of_larger_than_block in range(0,len(my_list) - 1):
				if my_list[end_of_larger_than_block + 1] < pivot:
					my_list[end_of_larger_than_block + 1], my_list[end_of_smaller_than_block + 1] = my_list[end_of_smaller_than_block + 1], my_list[end_of_larger_than_block + 1]
					end_of_smaller_than_block += 1

			my_list[0], my_list[end_of_smaller_than_block] = my_list[end_of_smaller_than_block], my_list[0]

			first_part = self.Quicksort(my_list[:end_of_smaller_than_block])
			second_part = self.Quicksort(my_list[end_of_smaller_than_block + 1:])
			first_part.append(my_list[end_of_smaller_than_block])
			return first_part + second_part

# Driver code

quicksort = Quicksort()
my_list = list(range(1000000))
random.seed()
random.shuffle(my_list)
start = time.time()
quicksort.Quicksort(my_list)
end = time.time()
print(end-start)