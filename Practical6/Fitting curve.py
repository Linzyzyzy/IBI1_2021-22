from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import numpy as np

# design fitting curve
def func(x, a, b, c):
    return a * x * x + b * x + c

# input variables
xdata = np.array([30.00,35.00,40.00,45.00,50.00,55.00,60.00,65.00,70.00,75.00])
ydata = np.array([1.03,1.07,1.11,1.17,1.23,1.32,1.42,1.55,1.72,1.94])
# draw the origin curve
plt.plot(xdata, ydata, 'b-')
popt, pcov = curve_fit(func, xdata, ydata)

# for each x, we get the y2 in the fitting curve
y2 = [func(i, popt[0], popt[1], popt[2]) for i in np.linspace(30, 75, 10)]
# draw the fitting curve
plt.plot(np.linspace(30, 75, 10), y2, 'r--')
# output the coefficients of fitting curve
print(popt)

# show the plot
plt.show()


