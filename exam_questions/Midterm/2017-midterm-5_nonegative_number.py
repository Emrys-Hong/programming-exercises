#Design an efficient algorithm that determines the number of ways 5 non-negative integers can sum up to N. Your code must be able to handle large N values (150+) under 20 seconds. 

####brute force
def nos(n):
 ans = 0   
 for i in range(n+1): # a nested for loop for every non-negative integer given
    for j in range(n+1):
        for k in range(n+1):
            for l in range(n+1):
                for m in range(n+1): # cancer
                    if i + j + k + l + m == n:
                        ans += 1
 return ans
 
 ####method 1
 def nos(n, x = 5): # x represents number of non-negative integers to work with... note that we can easily work with more than 5 here
    if x == 1:
        return 1 # common sensical
    if n == 0:
        return 1 # this too
    else:
        solutions = 0    
        for i in range(x):
            for j in range(n):
                solutions += nos(j, i)
        return solutions
        
####method 2
def memo_nos(f): # Credits to CH3 for donating this portion
    nos_ans = {} # Yay, dictionaries!
    def helper_nos(*args):
        if str(args) not in nos_ans:
            nos_ans[str(args)] = f(args[0],args[1])  
        return nos_ans[str(args)]
    return helper_nos
@memo_nos
def nos(n, x = 5):
    if x == 2: # results for x == 2 is straight forward too and it cuts run time even more than x == 1
      return (n+1)
    if n == 0:
        return 1 # this too
    else:
        solutions = 0    
        for i in range(x):
            for j in range(n):
                solutions += nos(j, i)
        return solutions
####method 3
from scipy.special import comb
def nos(n, x=5):
 return comb(n+x-1 , x-1, exact=False, repetition=False)
