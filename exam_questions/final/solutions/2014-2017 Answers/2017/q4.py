def get_products(inlist, test):
	output_d = {} # Initialize output dictionary as empty
	second_output = [] # list of tuples that have test as the product
	for item in inlist:
		# Calculate product of entries
		product = 1
		for number in item:
			product *= number

		# If product is equal to test, add it to the second output list
		if product == test:
			second_output.append(item)

		# Add to output dictionary
		if product in output_d:
			# If it exists, append it
			output_d[product].append(item)
		else:
			# Otherwise, start a new list
			output_d[product] = [item]

	if len(second_output) == 0:	
		return (output_d, None)
	else:
		return (output_d, second_output)

inlist = [(3,5), (2,2), (2,2,3), (12,2), (7,3), (3,7,1)]

d,o = get_products(inlist, 15) 
print sorted(d.keys()) #== [4,12,15,21,24]
print sorted(d.values()) #== [[(2,2)], [(2,2,3)], [(3,5)], [(7,3),(3,7,1)], [(12,2)]]
print o #== [(3,5)]
d,o = get_products(inlist, 21) 
print o #== [(7,3),(3,7,1)]
d,o = get_products(inlist, 11) 
print o #== None