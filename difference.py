
A = [3, 1, 2, 4, 3]
B = []

# Here you don't need to do this cause the statement A = [3, 1, 2, 4, 3] will do exatly the same!
# A[0] = 3
# A[1] = 1
# A[2] = 2
# A[3] = 4
# A[4] = 3

def difference(x, y):
	return abs(x - y)

for number in A:
	a = A[0]
	b = A[1] + A[2] + A[3] + A[4]

B.append(difference(a, b))

for number in A:
	c = A[0] + A[1]
	d = A[2] + A[3] + A[4]

B.append(difference(c, d))

for number in A: 
	e = A[0] + A[1] + A[2]
	f = A[3] + A[4]

B.append(difference(e, f))

for number in A:
	g = A[0] + A[1] + A[2] + A[3]
	h = A[4]

B.append(difference(g, h))

B.sort()
print(B[0])


