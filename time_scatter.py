# This snippet creates a scatterplot with time as a color-coded dimension
# This is very useful for timeseries when correlation between two time-series changes in time
# Brilliant! 

improt matplotlib.pyplot as plt

fig, axs = plt.subplots(1, 2)

# Make a line plot for each timeseries
axs[0].plot(x, c='k', lw=3, alpha=.2)
axs[0].plot(y)
axs[0].set(xlabel='time', title='X values = time')

# Encode time as color in a scatterplot
axs[1].scatter(x_long, y_long, c=np.arange(len(x_long)), cmap='viridis')
axs[1].set(xlabel='x', ylabel='y', title='Color = time')
