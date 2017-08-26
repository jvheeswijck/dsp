# The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

import csv

def read_data(filename):  
    list_table = []    
    with open(filename, 'r') as f:
        csv_r = csv.reader(f, delimiter=',')
        for row in csv_r:
            list_table.append(row)            

    list_table.pop(0)
    return list_table

def get_index_with_min_abs_score_difference(goals):
    dif_list = [abs(int(x[5]) - int(x[6])) for x in goals]
    return dif_list.index(min(dif_list))

def get_team(index_value, parsed_data):
    return parsed_data[index_value][0]

football_table = read_data('python/football.csv')
print(str(get_team(get_index_with_min_abs_score_difference(football_table), football_table)))