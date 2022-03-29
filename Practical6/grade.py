import matplotlib.pyplot as plt

# input the marks
marks = [45,36,86,57,53,92,65,45]
# sort the marks
marks.sort()
# output the marks
print(marks)

# draw the boxplot of the marks
plt.boxplot(marks, showfliers=True, patch_artist=True)
plt.show()

# judge whether you pass or not
avg = sum(marks) / len(marks)
if avg >= 60:
    print("congratulations!")
if avg < 60:
    print("You Die")
