#Data Project: Solo
#Decription: Analysis of a CSV document containing information about UFO sightings throughout the US. I am analyzing how many UFO sightings occur per state, creating a bar graph to represent that data, stating which state has the most UFO sightings, and analyzing which shape most people describe the UFO as. I am using PANDAS to analyze my data.
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
print (ufo_counts)

#which state has the most ufo sightings?

max_state= ufo_counts.idxmax()
max_sightings= ufo_counts.max()
print("The state with the most UFO sightings is", max_state, "with " + str(max_sightings) + " UFO sightings.")

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