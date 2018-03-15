
# coding: utf-8

# In[14]:


class A:
    def foo(self,x):
        print ("executing foo(%s,%s)"%(self,x))

    @classmethod
    def class_foo(cls,x):
        print ("executing class_foo(%s,%s)"%(cls,x))

    @staticmethod
    def static_foo(x):
        print ("executing static_foo(%s)"%x)    

a=A()
a.foo(1)


# In[22]:


# midterm practice problem
def compress(mylist):
    outlist = []
    total = 0
    for i in mylist:
        if type(i) == int:
            total += i
        else:
            outlist.append(total)
            outlist.append(compress(i))
            total = 0 
    if total != 0:
        outlist.append(total)
    return outlist

list1 = [1,[2,3],4,[5,[6,[7,8],9],10],11,[12,13]]
list2 = [1,2,3,4,5]
print(compress(list1))


# In[24]:


def list_counter(base,digit):
    total = 0
    for i in digit[:-1]:
        total += i
        total *= base
    total += digit[-1]
    return total

print(list_counter(4,[1,2,3,0,1]))


# In[37]:


with open('/Users/MH/Desktop/user-info.txt','r') as f:
    files = f.readlines()
    mydict = {}
    
    for i in files:
        i = i[:-1]
        
        mylist = i.split()
        
        mydict[mylist[0]] = mylist[2:]
print(mydict)
def mutual_friends(user1,user2):
    return [i for i in mydict[user1] if i in mydict[user2]]
print(mutual_friends('A','P'))


# In[42]:


with open('/Users/MH/Desktop/user-info.txt','r') as f:
    files = f.readlines()
    mydict = {}
    
    for i in files:
        i = i[:-1]
        
        mylist = i.split()
        
        mydict[mylist[0]] = mylist[2:]:
    files = f.readlines()
    mydict = {}
    
    for i in files:
        i = i[:-1]
        
        mylist = i.split()
        
        mydict[mylist[0]] = mylist[1]
print(mydict)
def login():
    user_id = input('enter your user id:')
    password = input('enter your password:')
    if user_id in mydict:
        if password == mydict[user_id]:
            return 'Welcome'
        else:
            return 'your password is not {}'.format(password)
    else:
        return 'we dont have your account'
login()


# In[51]:


def sign_up():
    user_name = input('your user account:')
    password = input('put your password:')
    print(mydict)
    if user_name in mydict:
        return 'we have already have your account'
    with open('/Users/MH/Desktop/user-info.txt','a') as f:
        f.write('\n')
        f.write(user_name+' '+password)

sign_up()


# In[96]:


def count_change(amount):
    i = 0
    while amount >= 2**i:
        i += 1
    
    
    total = 1
    list1 = []
    while amount != 0 and i > -1:
        if amount >= 2**i:
            amount -= 2**i
            total *= get_number(2**i)
            
            list1.append(i)
        i -= 1

    
    for i in list1[1:-1]:
        
        total -= get_number(2**i)
    return total

def get_number(n):
    total = 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 4:
        return 4
    else:
        return get_number(n/2)**2/2 - get_number(n/2)/2 + 1
    
print(count_change(9))


# In[90]:


def count_change(amt):
    binary_list = [2 ** x for x in range(20)]
    
    amt_list = [amt]
    iterator = 0
    
    while amt_list[-1] > 1:
    
        highest_divisor = None
    
        for i in binary_list[::-1]:
            if amt_list[iterator] % i < amt_list[iterator]:
                highest_divisor = i
                amt_list.append(amt_list[iterator] - highest_divisor)
                amt_list[iterator] = highest_divisor
                iterator += 1
                break
    
    if amt_list[-1] == 0:
        amt_list.pop()
        
    result = 1
    
    for i in range(len(amt_list)):
        if i != 0:
            result *= amt_list[i]
        else:
            result *= (amt_list[i] - 1)
    return result
print(count_change(9))

