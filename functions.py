import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

def regressionLine(x,y, text_place_x, text_place_y):

    slope, intercept, r_value, p_value, std_err = linregress(x, y)

    print("R-squared: %f" % r_value**2)
    plt.plot(x, intercept + slope*x, 'r', label='regression line')
    plt.text(text_place_x, text_place_y, f'y = {round(slope,3)}x + {round(intercept,3)}', color = 'red', fontsize = 12)
    plt.legend()

def scatterDraw(xValue, yValue, frame, color):
    plt.figure(figsize=(14, 6))
    plt.scatter(frame[xValue], 
            frame[yValue], 
            color=color)
    plt.xlabel(xValue)
    plt.ylabel('COVID Mortality Ratio-(Positive Cases / Deaths)')

def stateGrouper(groupByField, num_of_bins, dataFrame):
    dataFrame = dataFrame.sort_values(groupByField)
    dataFrame.index = np.arange(1, len(dataFrame) + 1)
    dataFrame[f'{groupByField}_bin'] = np.ceil(dataFrame.index / (len(dataFrame) / num_of_bins)).astype(int)
    return dataFrame

def boxDraw(groupByField, num_of_bins, dataFrame):
    fig1, ax1 = plt.subplots()
    ticks = [*range(1,num_of_bins+1)]

    collection = []
    labels = ticks
    for box in set(dataFrame[f'{groupByField}_bin']):
        collection_df = dataFrame.loc[(dataFrame[f'{groupByField}_bin'] == box)]
        collection.append(collection_df['Mortality Rate'].tolist())
        
    plt.boxplot(collection, patch_artist=True, flierprops=dict(marker='o', markerfacecolor='r')
                     , medianprops= dict(color='white', linewidth=2)
                     , boxprops = dict(facecolor = '#235574'))
    ax1.set(facecolor = '#c0c0c0' )
    plt.xticks(ticks, labels)

    ax1.set_title(f'{groupByField} vs COVID Mortality')
    ax1.set_ylabel('COVID Mortality Ratio-(Positive Cases / Deaths)')
    ax1.set_xlabel(f'{groupByField}ed State Groups from Best to Worst')