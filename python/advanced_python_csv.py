import csv

with open(r'python/faculty.csv', 'r') as f:
    csv_f = csv.reader(f)
    faculty = [row for row in csv_f]

headers = faculty.pop(0)
emails = [x[3] for x in faculty]

with open(r'python/emails.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    for row in emails:
        writer.writerow([row])
