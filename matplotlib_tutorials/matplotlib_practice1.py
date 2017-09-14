import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 5, 11)
y = x ** 2

print('X\n', x)
print('Y\n', y)

# Plot out the x and y coordinates
plt.plot(x, y, 'r') # 'r' is the color red
plt.xlabel('X Axis Title')
plt.ylabel('Y Axis Title')
plt.title('String Title')
plt.show()

# creating multiplots on same canvas
# plt.subplot(nrows, ncols, plot_number)
# you can even plot both subplots on the same plot_number
plt.subplot(1,2,1)
plt.plot(x, y, 'r--')

plt.subplot(1,2,2)
plt.plot(y, x, 'g*-')

###############

# Object Oriented Method
# Create a figure first. Synonym to a canvas
fig = plt.figure()

# Add set of axes to figure
# Think of axes as size and position of the space where you're plotting
axes = fig.add_axes([0.1,0.1,0.8,0.8])   # Left, bottom, width, height (range 0 to 1)

# plot on that set of axes
axes.plot(x,y,'b')
axes.set_xlabel('X Label')
axes.set_ylabel('Y Label')
axes.set_title('String Title')
plt.show()

# Now create 2 axes and plot them on the same figure
axes1 = fig.add_axes([0.1,0.1,0.8,0.8])
axes2 = fig.add_axes([0.2,0.5,0.4,0.3])

# Larger Axes 1
axes1.plot(x,y,'b')
axes1.set_xlabel('Time')
axes1.set_ylabel('Money')
axes1.set_title('Time vs Money')

# Smaller Axes 2
axes2.plot(y,x,'r')
axes2.set_xlabel('Money')
axes2.set_ylabel('Happyness')
axes2.set_title('Money vs Happyness')

#############

# Subplots Object, which act as a more automatic axis manager
fig, axes = plt.subplots()

# Use the Axes object to add details to the plot
axes.plot(x,y,'r')
axes.set_xlabel('X Label Here')
axes.set_ylabel('Y Label Here')
axes.set_title('Title Here')

# You can specify the number of rows and columns when creating the subplots() object
# Empty canvas of 1 by 2 subplots
# figsize is a tuple of the width and height of the figure in inches
# dpi is the dots-per-inch (pixel per inch), kind of like size
fig, axes = plt.subplots(figsize=(12,6), dpi=100, nrows=1, ncols=2)

# Axes is actually an array of axes to plot on
# Thus you can iterate through it and set details for multiple arrays with a few loops
for ax in axes:
    ax.plot(x, y, 'g--')
    ax.set_xlabel('X here')
    ax.set_ylabel('Y here')
    ax.set_title('Title Me')

# Method to adjust the positions of the axes to avoid overlap
plt.tight_layout()
plt.show()

############

# Saving a figure in either PNG, JPG, EPS, SVG, PGF and PDF.
# Note, do not run plt.show() before fig.savefig()
fig.savefig("filename.png", dpi=200)

# Legends http://matplotlib.org/users/legend_guide.html#legend-location
fig = plt.figure()

ax = fig.add_axes([0,0,1,1])

ax.plot(x, x**2, 'b.-', label='x**2')
ax.plot(x, x**3, 'g--', label='x**3')
ax.legend()

ax.legend(loc=1) # upper right corner
ax.legend(loc=2) # upper left corner
ax.legend(loc=3) # lower left corner
ax.legend(loc=4) # lower right corner

# Most common to choose
ax.legend(loc=0) # let matplotlib decide the optimal location

##########

# Formatting
# Color can be set with the MatLab like syntax
ax.plot(x, x**2, 'b.-', label='X Squared')
ax.plot(x, x**3, 'g--', label='X Cubed')

# Or Color can be set with the color=parameter
ax.plot(x, x**2, color="blue", alpha=0.5, label='X Squared')   # half-transparent
ax.plot(x, x+2, color="#8B008B")   # RGB hex code

# Linewidth (lw) and Linestyle (ls)
# possible linestype options ‘-‘, ‘–’, ‘-.’, ‘:’, ‘steps’
ax.plot(x, x**2, color="blue", alpha=0.5, linewidth=5, linestyle='-.', label='X Squared')
ax.plot(x, x**2, color="blue", alpha=0.5, lw=5, ls='-.', label='X Squared')

# Marker
# possible marker symbols: marker = '+', 'o', '*', 's', ',', '.', '1', '2', '3', '4', ...
ax.plot(x, x**2, color="blue", label='X Squared', marker='o', markersize=10,)
ax.plot(x, x**3, color="#FF8C00", label='X Cubed', marker='+')
ax.plot(x, x**2, color="blue", label='X Squared', marker='o', markersize=10,
        markerfacecolor='yellow', markeredgewidth=3)

#############

# Plot range and axes sizing
fig, axes = plt.subplot(1, 3, figsize=(12,6))

axes[0].plot(x, x**2, x, x**3)
axes[0].set_title("default axes ranges")

axes[1].plot(x, x**2, x, x**3)
axes[1].axis('tight')
axes[1].set_title("tight axes")

axes[2].plot(x, x**2, x, x**3)
axes[2].set_ylim([0, 60])
axes[2].set_xlim([2, 5])
axes[2].set_title('custom title range')

# http://www.matplotlib.org - The project web page for matplotlib.
# https://github.com/matplotlib/matplotlib - The source code for matplotlib.
# http://matplotlib.org/gallery.html - A large gallery showcaseing various types of plots matplotlib can create. Highly recommended!
# http://www.loria.fr/~rougier/teaching/matplotlib - A good matplotlib tutorial.
# http://scipy-lectures.github.io/matplotlib/matplotlib.html - Another good matplotlib reference.