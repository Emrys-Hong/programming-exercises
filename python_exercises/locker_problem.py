# this one is for the final exam Q9 for 2015 final

def open_locker(k):
    mylist = [0]*k
    for i in range(1,k+1):
        for j in range(0,k,i):
            mylist[j] = 1 if mylist[j] == 0 else 0
    return sum(mylist)

print(open_locker(48))