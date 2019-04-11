# Import the necessary pandas library for reading the CSV and using dataframes
import pandas as pd
# Import the necessary plotting library for our bar graph
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
# Import the Path module from the pathlib library to work with windows file paths
# Typically "\" is an escape character in a string and messes up the file paths.
from pathlib import Path
# Copy the path of the folder to the Path object. Make sure to replace all "\" with "/" first.
data_folder = Path('C:/blank/Python Scripts/source/repos/States_and_capitals_exercise/PythonApplication1')
# Apend the file name onto the end of the folder path with a "/" in between
file_to_open = data_folder / "us-state-capitals.csv"
# Import the data frame.
df = pd.read_csv(file_to_open)
# Print to check
print('Check the first few rows for correct entry.')
print(df.head(5))

# Create a class called state which will store the information from the data frame in
# attributes of this class.
class state(object):
    def __init__(self, name, capital, latitude, longitude):
        self.name = name
        self.capital = capital
        self.lat = latitude
        self.long = longitude

# This method will return the first letter of the name of the state
    def firstLetter(self):
        return(self.name[0])

# Create empty list to append each new class object to
list_states = []
# Iterate through each row in the df and create a new state object for it, then store
# these in a list.
for row in range(df.shape[0]):
    # Create an object for each row, state, in the df
    state_obj = state(df.iloc[row, 0], df.iloc[row, 1], df.iloc[row, 2], df.iloc[row, 3])
    # Append the new object to the list
    list_states.append(state_obj)

# Create a string of all the first letters of the state names
the_string = ''
for item in list_states:
    the_string += item.firstLetter()

# Count the number of times each letter occurs in the string
import collections
results = collections.Counter(the_string)

# Create a dictionary out of the results Counter object
# Create empty dictionary
final = {}
for item in results:
    final[item] = results[item]

# Create empty dataframe to store the counts.
df_letters = pd.DataFrame(index = range(26), columns = ['Letter', 'Count'])
# Print the results of counting letter by letter and add them to a dataframe
# Initialize counter variable at 0
counter = 0
for key in final:
    print("There are " + str(final[key]) + " " + key + "'s")
    # Add the counts to a data frame instead
    df_letters.loc[counter] = [key, final[key]]
    counter += 1

print('Check the first few rows for correct storage.')
print(df_letters.head(5))

# need to move to a jupiter notebook to visualize...
df_letters.plot(kind = 'bar')