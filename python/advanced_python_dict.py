import csv
import re

with open(r'python/faculty.csv', 'r') as f:
    csv_f = csv.reader(f)
    faculty = [row for row in csv_f]

headers = faculty.pop(0)

# Fix degree format
replace = [('Ph.?D.?', 'Ph.D. '), ('M.?S.?', 'M.S. '), 
            ('Sc.?D.?', 'Sc.D. '), ('M.?D.?', 'M.D. '),
            ('M.?D.?', 'M.D. '), ('M.?P.?H.?', 'M.P.H '),
            ('J.?D.?', 'J.D. '), ('M.?A.?', 'M.A. '),
            ]
for person in faculty:
    for pattern, result in replace:
        person[1] = re.sub(pattern, result, person[1])
    person[1] = person[1].strip()


faculty_dict = {person[0].rpartition(' ')[2]:person[1:] for person in faculty}

# Print 3 elements from the dictionary
for i, item in enumerate(faculty_dict.items()):
    print(item)
    if i == 2:
        break
print('--------------')

# Create dictionary with (First Name, Last Names) as key
names = [(person[0].rpartition(' ')[0], person[0].rpartition(' ')[2]) for person in faculty]
professor_dict = {name:details[1:] for name,details in zip(names,faculty)}

for i, item in enumerate(professor_dict.items()):
    print(item)
    if i == 2:
        break
print("----------------")

professors_sorted = sorted(professor_dict.items(), key=lambda x: x[0][1])

for i, item in enumerate(professors_sorted):
    print(item)
    if i == 5:
        break