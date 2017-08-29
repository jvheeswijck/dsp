import csv
import re
from collections import Counter

with open(r'python/faculty.csv', 'r') as f:
    csv_f = csv.reader(f)
    faculty = [row for row in csv_f]
    faculty.pop(0)


degrees = re.sub(r'[.]', '', ' '.join(x[1] for x in faculty)).split()
degrees_uniq = set(degrees)
degrees_uniq.remove('0')

# Q1. How many unique degrees and frequencies?
print(len(degrees_uniq))
print(Counter(degrees))
print('--------------------')

# Q2. How many unique titles and frequencies
titles = [re.sub(r'\bis\b', 'of', x[2]) for x in faculty]
print(set(titles))
print(Counter(titles))
print('--------------------')

# Q3. Print list of email addresses.
emails = [x[3] for x in faculty]
print(emails)
print(len(emails))
print('--------------------')

# Q4. 
emails_domains = set([x.split('@')[1] for x in emails])
print(len(emails_domains))
print(emails_domains)
print('--------------------')


