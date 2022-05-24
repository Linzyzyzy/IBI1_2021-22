# input the variables
a = 19245301
b = 4218520
c = 271
d = b - c
e = a - b
# output d and e
print(d)
print(e)
# compare with e and d
if e > d:
    print('e is bigger than d')
else:
    print('e is smaller than d')

X = True
Y = True
W = X and Y
print(W)
X = False
Y = False
W = X and Y
print(W)
X = True
Y = False
W = X and Y
print(W)