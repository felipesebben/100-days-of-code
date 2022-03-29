# # with open("weather_data.csv", 'r') as f:
# #     data = f.readlines()
# #     print(data)
# #     for row in data:
# #         stripped_row = data.strip()
# #         print(stripped_row)
#
# # Use csv to parse through the file.
# # import csv
# # with open('weather_data.csv', 'r') as f:
# #     data = csv.reader(f)
# #     temperatures = []
# #     print(data)
# #     for row in data:
# #         print(row)
# #     for row in data:
# #         if row[1] != 'temp':
# #             temperatures.append(int(row[1]))
# #     print(temperatures)
# #
#
import pandas as pd
#
# data = pandas.read_csv('weather_data.csv')
# # print(type(data)) # Returns pandas DataFrame object
# # print(data['temp'])
#
# # Convert data to dict
# # data_dict = data.to_dict()
# # print(data_dict)
#
# # temp_list = data['temp'].to_list()
# # print(len(temp_list))
# #
# # avg_temp = sum(temp_list) / len(temp_list)
# # print(avg_temp)
#
# # Print the average temperature in a simpler way using .mean().
# # print(data['temp'].mean())
#
# # Print the highest temperature
# # print(data['temp'].max())
#
# # Get data in columns.
# # print(data['condition'])
#
# # Alternatively, call data.condition. The key must follow capital letters.
# # print(data.condition)
#
# # Get data in rows.
# # print(data[data['day'] == 'Monday'])
# #
# # # Get the row with the highest recorded temperature.
# # print(data[data['temp'] == data['temp'].max()])
# #
# # monday = data[data['day'] == 'Monday']
# # monday_temp = int(monday['temp'])
# # monday_temp_f = (monday_temp * 9/5) + 32
# # print(monday_temp_f)
#
# # Create a dataframe from scratch
# data_dict = {
#     'students': ['Amy', 'James', 'Angela'],
#     'scores': [76, 56, 65]
# }
#
# data = pandas.DataFrame(data_dict)
# data.to_csv('new_data.csv')
#

data = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
grey_squirrels_count = len(data[data['Primary Fur Color'] == "Gray"])
red_squirrels_count = len(data[data['Primary Fur Color'] == "Cinnamon"])
black_squirrels_count = len(data[data['Primary Fur Color'] == "Black"])
print(grey_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

squirrels_dict = {
    'Fur Color': ['grey', 'red', 'black'],
    'Count': [grey_squirrels_count, red_squirrels_count, black_squirrels_count],
    }

squirrels_df = pd.DataFrame(squirrels_dict)
squirrels_df.to_csv("squirrels_count.csv")
print(squirrels_df)

