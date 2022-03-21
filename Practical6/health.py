import matplotlib.pyplot as plt

paternal_age = [30,35,40,45,50,55,60,65,70,75]
chd = [1.03,1.07,1.11,1.17,1.23,1.32,1.42,1.55,1.72,1.94]

# make a dictionary
pairs = {}
i = 0
for i in range(len(chd)):
    pairs[paternal_age[i]] = chd[i]

# make a plot
plt.scatter(paternal_age,chd)
plt.show()

father1 = 40
a = father1/5-6
risk = chd[int(a)]
print(f'relative risk to child is {risk}')


