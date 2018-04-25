import libdw.sm as sm
import copy

class CombLock(sm.SM):
    def __init__(self, keyList):
        self.keyList = keyList
        self.startState = []

    def getNextValues(self, state, inp):
        if inp == 0:
        	return (state, 'locked')
        elif inp >= 1 and inp <= 9:
            #add your code here
            newState = copy.copy(state)
            newState.append(inp)
            return (newState, 'locked')
        elif inp == -1:
            output = 'locked'
            if state == self.keyList:
            	output = 'unlocked'
            return ([], output)

lock = CombLock([1,2,5])
print lock.transduce([1,2,5,-1])
print lock.transduce([1,0,2,5,-1])
print lock.transduce([3,2,5,-1])
print lock.transduce([1,2,5,-1,1,2,5,-1])
print lock.transduce([3,2,5,-1,1,2,5,-1])

