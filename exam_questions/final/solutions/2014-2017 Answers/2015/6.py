import libdw.sm as sm

class Elevator(sm.SM):
	startState = 0 # start at the first floor

	def getNextValues(self, state, inp):
		newState = state
		if inp == 'Up':
			newState += 1
		elif inp == 'Down':
			newState -= 1

		# Limit state to be between 0 and 2 (1st and 3rd floor)
		newState = min(newState, 2)
		newState = max(newState, 0)

		floorNames = ["First", "Second", "Third"]
		return (newState, floorNames[newState])


e = Elevator()
print e.transduce( ['Up', 'Up', 'Up', 'Up', 'Down', 'Down', 'Down', 'Up']) == ['Second', 'Third', 'Third', 'Third', 'Second', 'First', 'First', 'Second']
