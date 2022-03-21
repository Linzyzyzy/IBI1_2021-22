import matplotlib.pyplot as plt

marks = [45,36,86,57,53,92,65,45]
print(marks)

plt.boxplot(marks, showfliers=True, patch_artist=True)
plt.show()

avg = sum(marks) / len(marks)
if avg >= 60:
    print("congratulations!")
if avg < 60:
    print("You Die")