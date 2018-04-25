def maxOccurrences(inp):
	inp_list = inp.split(' ') # change string into a list
	num_count = {} # dictionary to keep track how many times each number occurs

	for num_str in inp_list:
		num = int(num_str) # convert string to integer

		# If this number has appeared before, increment its count
		if num in num_count:
			num_count[num] += 1
		# Otherwise, initialize the count as 1
		else:
			num_count[num] = 1

	# Find maximum count
	max_numbers = []
	max_count = 0
	for num in num_count:
		# Occurs more times than current
		if num_count[num] > max_count:
			# Set new max
			max_numbers = [num]
			max_count = num_count[num]
		# Equal number of times, add to list
		elif num_count[num] == max_count:
			max_numbers.append(num)

	return (sorted(max_numbers), max_count)


print 'test 1'
inp='2 3 40 3 5 4 -3 3 3 2 0'
print maxOccurrences(inp)

print 'test 2'
inp='9 30 3 9 3 2 4'
print maxOccurrences(inp)