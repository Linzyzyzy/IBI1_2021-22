import matplotlib.pyplot as plt

# input the variables
paternal_age = [30,35,40,45,50,55,60,65,70,75]
chd = [1.03,1.07,1.11,1.17,1.23,1.32,1.42,1.55,1.72,1.94]

# make a dictionary
pairs = {}
i = 0
for i in range(len(chd)):
    pairs[paternal_age[i]] = chd[i]
# output the dictionary
print(pairs)

# make a plot
plt.scatter(paternal_age,chd)
plt.show()

# output specific value
father1 = int(input("The father's age: "))
a = father1/5-6
risk = chd[int(a)]
print(f'Relative risk to child is {risk}')


