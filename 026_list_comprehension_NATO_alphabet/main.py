# new_numbers = [new_item for item in list]
#
# numbers = [1, 2, 3]
# new_numbers = [n + 1 for n in numbers]
# print(new_numbers)
# # [2, 3, 4]
#
# name = "Felipe"
# new_list = [letter for letter in name]
# print(new_list)
# # ['F', 'e', 'l', 'i', 'p', 'e']
#
# sequence = range(1,5)
# new_sequence = [n * 2 for n in sequence]
# print(new_sequence)
# # [2, 4, 6, 8]
#
# names = ['Alex', 'Caroline', 'Eleanor', 'Dave', 'Beth', 'Freddie']
#
# short_names = [nam for nam in names if len(nam) < 5]
#
# uppercase_long_names = [nam.upper() for nam in names if len(nam) > 4]


student_dict = {
    'student': ['Angela', 'James', 'Lily'],
    'score': [56, 76, 98]
}

# for (key, value) in student_dict.items():
#     print(value)

# Loop in a DataFrame as if you were working with a dict.
import pandas as pd

student_df = pd.DataFrame(student_dict)
print(student_df)
#
# # Loop through a data frame
# for (key, value) in student_df.items():
#     print(value)

# Iter rows method - inbuilt method that allows you to iter through each of the rows.
for (index, row) in student_df.iterrows():
    # print(row['student']) # Each row is a pandas series object
    if row['student'] == 'Angela':
        print(row['score'])