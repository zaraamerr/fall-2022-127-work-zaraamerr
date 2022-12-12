import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset into a Pandas dataframe
df = pd.read_csv('ufo_sightings.csv')

#how many ufo sightings per state?
ufo_counts= df['Location.State'].value_counts()
print (ufo_counts)
#plot it

# how many ufo sightings per city?
# ufo_citycounts= df['Location.City'].value_counts()
# print(ufo_citycounts)