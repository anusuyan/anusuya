a = 0
    b = 1
    for i in range(0, n):
	temp = a
	a = b
	b = temp + b
    return a
for c in range(0, 15):
    print(fibonacci(c))
