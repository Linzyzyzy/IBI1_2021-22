# aim: we want to get 64 slices of pizza, and cut in least knives
# for n cut, we can get at most (n*n + n + 2)/2 slices
# so we create a cycle, if the slice "p" is smaller than the 64, the cut "n" will += 1
n = 0
p = 0
while p < 64:
    n += 1
    p = (n*n + n + 2)/2
print('we will get {} slices of pizza, for we cut {} knives'.format(p, n))