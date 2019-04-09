# Import the necessary pandas library for reading the CSV and using dataframes
import pandas as pd
# Import the Path module from the pathlib library to work with windows file paths
# Typically "\" is an escape character in a string and messes up the file paths.
from pathlib import Path
# Copy the path of the folder to the Path object. Make sure to replace all "\" with "/" first.
data_folder = Path('C:/Users/<username>/Desktop')
# Apend the file name onto the end of the folder path with a "/" in between
file_to_open = data_folder / "us-state-capitals.csv"
# Import the data frame.
capital_dic = pd.read_csv(file_to_open)
# Print to check
print(capital_dic)

# Create a class called state which will store the information from the data frame in
# attributes of this class.
def 

# Create empty list to append each new class object to
list_states = []
# Iterate through each key in the input dictionary
for key in capital_dic:
    # Create a mini_dic for each state storing the state name in 'state' and state capital in 'capital'
    dic_pairs = {'state':key, 'capital':capital_dic[key]}
    list_states.append(key)

# Create a string of all the first letters of the state names
the_string = ''
for state in list_states:
    the_string += state[0]

# Count the number of times each letter occurs in the string
import collections
results = collections.Counter(the_string)

# Create a dictionary out of the results Counter object
final = {}
for item in results:
    final[item] = results[item]
    print(type(item), type(results[item]))

print(final)


