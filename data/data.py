import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset into a Pandas dataframe

df = pd.read_csv('ufo_sightings.csv')

#check the column names of the df

print (df.columns)

#analyze how many ufo sightings per state?

ufo_counts= df['Location.City'].value_counts() #variable that counts sightings per state
print (ufo_counts)

#plot it
ufo_counts.plot(kind='bar')
plt.show() #show the plot, the x values is the location/state and the y values are the ufo sightings of that particular state.