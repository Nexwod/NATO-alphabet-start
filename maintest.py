student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

# import pandas
# student_data_frame = pandas.DataFrame(student_dict)

# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

import csv
import random
with open("nato_phonetic_alphabet.csv") as nato:
    nato_data=csv.reader(nato)
    alphabets= []
    nat = []
    for i in nato_data:
        nat.append(i[1])
        alphabets.append(i[0])
    # print(nat)
    # print(alphabets)
    n=0
    new_dic = {range(1, 10):i for i in nat}
 
    # print(new_dic)
    
    # print(nato_data[0])

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

