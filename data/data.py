#Data Project: Solo
#Decription: Analysis of a CSV document containing information about UFO sightings throughout the US. Things I analyzed: how many UFO sightings occur per state, which state has the most UFO sightings, which state has the least UFO sightings, and what the most common UFO shape was. I am using PANDAS to analyze my data.
#EXTRA 1: Use multiple aspects of a single data source in your analysis.
#EXTRA 2: Use Matplotlib or another Python graphing/plotting library to visualize part or all of your analysis.

import pandas as pd
import matplotlib.pyplot as plt

#BASE PROJECT

# Load the dataset into a Pandas dataframe

df = pd.read_csv('ufo_sightings.csv')

#check the column names of the df

df.columns

#analyze how many ufo sightings per state?

ufo_counts= df['Location.State'].value_counts() #variable that counts sightings per state
print (ufo_counts) #prints each state and their total UFO sightings

#which state has the most ufo sightings?

max_state= ufo_counts.idxmax() #determines the state with the most UFO sightings
max_sightings= ufo_counts.max() #determines the number of said UFO sightings
print("The state with the most UFO sightings is", max_state, "with " + str(max_sightings) + " UFO sightings.")

#which state has the least ufo sightings?

min_state= ufo_counts.idxmin() #determines the state with the least UFO sightings
min_sightings= ufo_counts.min() #determines the number of said UFO sightings
print("The state with the least UFO sightings is", min_state, "with " + str(min_sightings) + " UFO sightings.")

#EXTRA 1: Use multiple aspects of a single data source in your analysis: For this, I am analyzing which shape most people used to describe the UFO as.

#analyze which shape did most people describe the UFO as? 

shape_counts= df['Data.Shape'].value_counts()
print(shape_counts)

#which shape is the most common description of the UFO?

max_shape= shape_counts.idxmax()
print("Most people described the UFO as the shape of a " + max_shape)

#EXTRA 2: Use Matplotlib or another Python graphing/plotting library to visualize part or all of your analysis. For this, I am using matplotlib to graph the states and their respective total number of UFO sightings.

#plot
ufo_counts.plot(kind='bar')
plt.show() #show the plot, the x values is the location/state and the y values are the number of ufo sightings. The bar graph aims to show how many UFO sightings occurred in each state.

#done w/ project.