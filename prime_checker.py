####Design an efficient algorithm to determine if# a positive integer N is a prime number. Your code must be able to process large N values (above half billion) under 20 seconds.


def is_prime(N):
    return N > 1 and all(N % i for i in range(2, int(N**.5), 2)) # check only till the nearest square root of N; skipping all even numbers.


import random
def isPrime(n, k=999): # miller-rabin ; Accuracy increases as k increases
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True
    
 '''Checks under 5 seconds: n = 94366396730334173383107353049414959521528815310548187030165936229578960209523421808912459795329035203510284576187160076386643700441216547732914250578934261891510827140267043592007225160798348913639472564715055445201512461359359488795427875530231001298552452230535485049737222714000227878890892901228389026881

is a prime number.

 '''
