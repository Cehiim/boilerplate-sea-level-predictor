import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']

    plt.scatter(x, y, s=5)

    # Create first line of best fit
    line = linregress(x, y)
    x_prediction = range(1880, 2051)
    y_prediction = line.slope * x_prediction + line.intercept

    plt.plot(x_prediction, y_prediction, linestyle='-', color='red', label='Prediction using data from 1880-2013')

    # Create second line of best fit
    filtered_df = df.loc[df['Year'] >= 2000]
    new_x = filtered_df['Year']
    new_y = filtered_df['CSIRO Adjusted Sea Level']
    new_line = linregress(new_x, new_y)
    new_x_prediction = range(2000, 2051)
    new_y_prediction = new_line.slope * new_x_prediction + new_line.intercept

    plt.plot(new_x_prediction, new_y_prediction, linestyle='-', color='purple', label='Prediction using data from 2000-2013')
    plt.ylim(-1, 20)
    plt.legend()

    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()