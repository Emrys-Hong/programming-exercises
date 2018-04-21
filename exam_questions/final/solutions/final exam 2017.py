def complete_ISBN(string):
    total = 0
    for i in range(len(string)):
        total += (i+1)*int(string[i])
    total %= 11
    total = str(total) if total < 10 else 'X'
    return string+total
# print(complete_ISBN('013031997'))

def get_products(inlist,test):
    import numpy as np
    mydict = {}
    for i in inlist:
        if np.product(np.array(i)) not in mydict.keys():
            mydict[np.prod(np.array(i))] = [i]
        else:
            mydict[np.prod(np.array(i))].append(i)

    o = mydict[test] if test in mydict.keys() else None
    return mydict, o

# inlist = [(3,5),(2,2),(2,2,3),(12,2),(7,3),(3,7,1)]
# d, o = get_products(inlist,15)
#
# print(sorted(d.keys()))
# print(sorted(d.values()))
# print(o)

#################### Q5
from libdw import sm
class SpellCheckSM(sm.SM):
    start_state = 'new word'
    def get_next_values(self,state,inp):
        con = 'kgstdnhbmr'
        vow = 'aeiou'
        if state == 'new word':
            if inp in con:
                state = 'consonant'
                output = ''
            elif inp not in con and inp != ' ':
                state = 'error'
                output = ''
            elif inp == ' ':
                state = 'new word'
                output = ''
        elif state == 'consonant':
            if inp in vow:
                state = 'vowel'
                output = ''
            elif inp == ' ':
                state = 'new word'
                output = 'error'
            elif inp != ' ' and inp not in vow:
                state = 'error'
                output = ''
        elif state == 'vowel':
            if inp == ' ':
                state = 'new word'
                output = 'ok'
            else:
                state = 'error'
                output = ''
        elif state == 'error':
            if inp == ' ':
                state = 'new word'
                output = 'error'
            else:
                state = 'error'
                output = ''
        return state, output
#
# a = SpellCheckSM()
# line = 'a si tu ne mai me pas je '
# print(a.transduce(line))

class Parallelogram:
    def __init__(self,side1,side2,diagonal):
        self.side1 = side1
        self.side2 = side2
        self.diagonal = diagonal
    def __str__(self):
        return str(round(float(self.diagonal*1.00),2))

    def getter(self):
        return self._diagonal
    def setter(self,x):
        if x >= 0:
            self._diagonal = x
        else:
            self._diagonal = 0
    diagonal = property(getter,setter)
    def __call__(self):
        if self.diagonal >= self.side2+self.side1:
            return False
        else:
            return True

    def calc_area(self):
        s = (self.side2 + self.side1 + self.diagonal) / 2
        area = round(2 * (s * (s - self.side1) * (s - self.side2) * (s - self.diagonal)) ** 0.5, 2)
        return str(area)

class Rectangle(Parallelogram):
    def __call__(self):
        if (self.side1+self.side2)**0.5 == self.diagonal:
            return True
        else:
            return False
class Rhombus(Parallelogram):
    def __call__(self):
        if (self.side2 == self.side1) and (self.side1+self.side2<self.diagonal):
            return True
        else:
            return False
class Square(Parallelogram):
    def __call__(self):
        if (self.side2 == self.side1) and (self.side1+self.side2>self.diagonal) and ((self.side1**2+self.side2**2)**0.5==self.diagonal):
            return True
        else:
            return False
# para = Parallelogram(2,3,4)
# print(para)
# para.diagonal = -1
# print(para)
# squr = Square(2,2,8**0.5)
# print(squr())
class MyTask(object):
    def __init__(self,deadline,duration):
        self.deadline = deadline
        self.duration = duration
assignments = [MyTask(14,10),MyTask(33,2),MyTask(14,1),MyTask(10,2),MyTask(5,3)]
assignments2 = [MyTask(3,2),MyTask(3,2)]
def getkey(mytask):
    return mytask.deadline
def procrastination(assignments):
    assignments = sorted(assignments,key=getkey,reverse=True)
    print([getkey(i) for i in assignments])
    time = assignments[0].deadline
    for task in assignments:
        if task.deadline < time:
            time = task.deadline - task.duration
        else:
            time = time - task.duration
        print(time)
    return time


# print(procrastination(assignments2))