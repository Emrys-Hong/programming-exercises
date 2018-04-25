def complete_ISBN(ins):
	total = 0
	# Loop through each character
	for i in range(len(ins)):
		digit = int(ins[i]) # Get the current digit as an integer
		total += digit * (i + 1) # Add it to the checksum using the formula

	# Compute checksum
	checksum = total % 11

	if checksum == 10:
		checksum = 'X'

	# Return full 10 digit number
	return ins + str(checksum)


# print 'Test case 1: ins=013601267'
print complete_ISBN('013601267') == "0136012671"

# print 'Test case 2: ins=013031997'
print complete_ISBN('013031997') == "013031997X"

# print 'Test case 3: ins=020139829'
print complete_ISBN('020139829') == "020139829X"