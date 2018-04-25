def compTrace(A):
	n = len(A)

	# Trace only exists for square matrices
	if n == len(A[0]):
		trace = 0
		for i in range(n):
			trace += A[i][i]

		return trace

	return None

A = [[2.2, 2, 3.1], [4, 5, 6], [7, 8, 9]]
print compTrace(A)
