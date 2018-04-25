import libdw.sm as sm

def mapT2P(x,y):
    if 0 <= x and x <= 3:
        if 0 <= y and y <= 3:
            return 1
        if 4 <= y and y <= 7:
            return 4
        if 8 <= y and y <= 11:
            return 7
    if 4 <= x and x <= 7:
        if 0 <= y and y <= 3:
            return 2
        if 4 <= y and y <= 7:
            return 5
        if 8 <= y and y <= 11:

          return 8
    if 8 <= x and x <= 11:
        if 0 <= y and y <= 3:
            return 3
        if 4 <= y and y <= 7:
            return 6
        if 8 <= y and y <= 11:
            return 9

class TouchMap(sm.SM):
    startState = 0 # stores the last virtual point number
    def getNextValues(self, state, inp):
        (e,x,y) = inp
        virtPointNum = mapT2P(x, y)
        if e == "TouchDown" or e == "TouchUpdate":
            if state == virtPointNum:
                return (virtPointNum, 0)
            else:
                return (virtPointNum, virtPointNum)
        else:
            return (virtPointNum, -1)


m = TouchMap()
print m.transduce([('TouchDown',2,2), ('TouchUpdate',3,3), ('TouchUp',4,4)])
print m.transduce([('TouchDown',3,3), ('TouchUpdate',4,3), ('TouchUp',4,4)])

