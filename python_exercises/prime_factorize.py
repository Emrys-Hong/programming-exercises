# this function find all the integers that will be the prime factor for i
def find_factor(n):
    mylist = []
    for i in range(2,int(n**0.5)+1):

        while n%i == 0:
            n /= i
            mylist.append(i)
    if n != 1:
        mylist.append(n)
    return mylist

print(find_factor(10000))