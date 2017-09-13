import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 5, 11)
y = x ** 2

print('X\n', x)
print('Y\n', y)

# plot out the x and y coordinates
# plt.plot(x, y, 'r') # 'r' is the color red
# plt.xlabel('X Axis Title')
# plt.ylabel('Y Axis Title')
# plt.title('String Title')
# plt.show()

# creating multiplots on same canvas
# plt.subplot(nrows, ncols, plot_number)
# plt.subplot(1,2,1)
# plt.plot(x,y,'r--')
#
# plt.subplot(1,2,2)
# plt.plot(y,x,'g*-')

# object oriented method
# create a figure first
fig = plt.figure()
#
# # add set of axes to figure
# axes = fig.add_axes([0.1,0.1,0.8,0.8])   # Left, bottom, width, height (range 0 to 1)
#
# # plot on that set of axes
# axes.plot(x,y,'b')
# axes.set_xlabel('X Label')
# axes.set_ylabel('Y Label')
# axes.set_title('String Title')
# plt.show()
#
axes1 = fig.add_axes([0.1,0.1,0.8,0.8])
axes2 = fig.add_axes([0.2,0.5,0.4,0.3])

# Larger Figure Axes 1
axes1.plot(x,y,'b')
axes1.set_xlabel('Time')
axes1.set_ylabel('Money')
axes1.set_title('Time vs Money')

# Smaller Figure Axes 2
axes2.plot(y,x,'r')
axes2.set_xlabel('Money')
axes2.set_ylabel('Happyness')
axes2.set_title('Money vs Happyness')

plt.show()