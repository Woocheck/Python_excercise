import matplotlib.pyplot as plt
import matplotlib.ticker as plticker

fig,ax=plt.subplots()

#Spacing between each line
intervals = float(5)

loc = plticker.MultipleLocator(base=intervals)
ax.xaxis.set_major_locator(loc)
ax.yaxis.set_major_locator(loc)

# Add the grid
ax.grid(which='major', axis='both', linestyle='-')