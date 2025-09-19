import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    regr_all  = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

    x_pred_all = np.arange(df['Year'].min(), 2051, 1)

    y_pred_all = regr_all.slope * x_pred_all + regr_all.intercept

    ax.plot(x_pred_all, y_pred_all, 'r', label='Best Fit Line (All Data)')

    # Create second line of best fit
    df2 = df[df['Year'] >= 2000]

    regr_2 = linregress(df2['Year'], df2['CSIRO Adjusted Sea Level'])

    x_pred_2 = np.arange(2000, 2051, 1)

    y_pred_2 = regr_2.slope * x_pred_2 + regr_2.intercept

    ax.plot(x_pred_2, y_pred_2, 'g', label='Best Fit Line (Since 2000)')


    # Add labels and title
    ax.set_title('Rise in Sea Level')
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.legend()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()