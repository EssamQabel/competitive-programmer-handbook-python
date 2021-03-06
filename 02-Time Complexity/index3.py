## CALCULATION RULES
# Loops
# O(n)
for i in range(100): # better to use xrange
	print(i)

# O(n^2)
for i in range(100):
	for j in range(100):
		print(i, j)

# MAXIMUM SUBARRAY SUM
arr = [-1, 2, 4, -3, 5, 2, -5, 2]

# O(n^3) solution
best = 0
for i in arr:
	for j in arr:
		sum = 0
		for k in arr:
			sum += k
		best = max(best, sum)
print(best)

# O(n^2) solution
best = 0
for i in range(len(arr)):
	sum = 0
	for j in range(i, len(arr)):
		sum += arr[j]
		best = max(best, sum)
print(best)

# O(n) solution
best, sum = 0, 0
for i in arr:
	sum = max(i, sum + i)
	best = max(best, sum)
print(best)
