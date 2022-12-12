#Data Project: Solo
#Decription: Analysis of a CSV document containing information about UFO sightings throughout the US. I am analyzing how many UFO sightings occur per state, creating a bar graph to represent that data, and stating which state has the most UFO sightings. I am using PANDAS to analyze my data.
#EXTRA 1: Use Matplotlib or another Python graphing/plotting library to visualize part or all of your analysis.

import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset into a Pandas dataframe

df = pd.read_csv('ufo_sightings.csv')

#check the column names of the df

print (df.columns)

#analyze how many ufo sightings per state?

ufo_counts= df['Location.State'].value_counts() #variable that counts sightings per state
print (ufo_counts)

#which state has the most ufo sightings?

max_state= ufo_counts.idxmax()
max_sightings= ufo_counts.max()
print("The state with the most UFO sightings is", max_state, "with " + str(max_sightings) + " UFO sightings.")

#plot it
ufo_counts.plot(kind='bar')
plt.show() #show the plot, the x values is the location/state and the y values are the number of ufo sightings. The bar graph aims to show how many UFO sightings occurred in each state.

