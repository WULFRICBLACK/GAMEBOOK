# import pandas
# print(pandas.read_csv('our book.csv', sep=';'))
# import csv
#
# with open('our book.csv', mode='w') as employee_file:
#     employee_writer = csv.writer(employee_file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#
#     employee_writer.writerow(['John Smith', 'Accounting', 'November'])
#     employee_writer.writerow(['Erica Meyers', 'IT', 'March'])

import json

with open("book.json") as read_file:
    data = json.load(read_file)
del data["additional improvements"]

print(json.dumps(data, indent=2))
