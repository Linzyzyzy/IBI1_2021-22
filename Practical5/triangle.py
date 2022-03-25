# cycle for 10 times, each time add 1,2,3,...,n to a, then output a
for n in range(1, 11):
	# initialize i,a
	i = 0
	a = 0
	for i in range(1, n + 1):
		a = a + i
	print(a)
