import matplotlib.pyplot as plt
xpoints = [1, 4,5,6,7]
ypoints = [2,6,3,6,3]

plt.title("Display marker")
plt.xlabel("x-axis")
plt.ylabel("y-axis")

plt.plot(xpoints, ypoints,'o:r',mfc='b')
plt.ylim(ymin=1)
plt.show()