from libdw import sm

def dec_to_bin(dec):
	''' Returns 3 bit binary representation of a decimal number '''
	if dec >= 0 and dec < 8:
		new_dec = dec # Keep a variable that can be edited locally
		bin_str = ""
		for i in range(2, -1, -1):
			value = 2 ** i
			if new_dec >= value:
				new_dec -= value
				bin_str += '1'
			else:
				bin_str += '0'

		return bin_str


class RingCounter(sm.SM):
	startState = 0 # keeps count in decimal

	def getNextValues(self, state, inp):
		if inp == 1:
			# Reset signal
			return (0, '000')
		else:
			# Increment
			state += 1
			# If state is more than 7, set it to 0
			state %= 8

			# Return binary representation
			return (state, dec_to_bin(state))

print 'test 1'
r=RingCounter()
print r.transduce([0,0,0,0,0,0,0,0,0]) == ['001', '010', '011', '100', '101', '110', '111', '000', '001']

print 'test 2'
r=RingCounter()
print r.transduce([0,0,0,1,0,0,0,0,0]) == ['001', '010', '011', '000', '001', '010', '011', '100', '101']

print 'test 3'
r=RingCounter()
print r.transduce([0,0,0,1,0,0,1,0,0]) == ['001', '010', '011', '000', '001', '010', '000', '001', '010']
