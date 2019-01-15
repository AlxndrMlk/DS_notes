def visualize_coefficients(x, y, ax):
    ax.bar(x, y)
    ax.set(xlabel='X label', ylabel='Y label')
    
    # Set formatting so it looks nice
    plt.setp(ax.get_xticklabels(), rotation=45, horizontalalignment='right')
    return ax
