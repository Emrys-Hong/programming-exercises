def getDivisors(n):
	return [i for i in range(1, n + 1) if n % i == 0]

def countNumOpenLockerBrute(K):
	lockersOpened = 1

	for i in range(2, K + 1):
		divisors = getDivisors(i)
		if len(divisors) % 2 != 0:
			lockersOpened += 1
	return lockersOpened

def countNumOpenLocker(K):
	count = 1
	newK = 0
	while newK < K:
		count += 1
		newK += count * 2 + 1
	return count

# print countNumOpenLockerBrute(100)
print countNumOpenLocker(1000000)
# print getDivisors(10)
# print countNumOpenLocker(2000) #returns 44
# print countNumOpenLocker(10) #returns 3
# print countNumOpenLocker(20) #returns 4