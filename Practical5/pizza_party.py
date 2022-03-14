n = 0
p = 0
while p < 64:
    n += 1
    p = (n*n + n + 2)/2
print('we will get {} slices of pizza, for we cut {} knives'.format(p, n))