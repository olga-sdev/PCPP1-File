"""
create and save data in csv -> open() with 'w' write parameter and csv.writer()
writerow() -> write each row into csv

quoting for read and  write ->
* csv.QUOTE_MINIMAL - only values with special characters such as separator or quotechar will be quoted
* csv.QUOTE_ALL – quotes all values
* csv.QUOTE_NONNUMERIC – quotes only non-numeric values
* csv.QUOTE_NONE – doesn't quote any values

DictWriter -> add data in format of dictionary
Additional information https://realpython.com/python-csv/
"""

import csv

with open('items.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter='|', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)

    writer.writerow(['Workshop Kit', '51'])
    writer.writerow(['A3 Building Plate', '24'])

"""
"Workshop Kit"|"51"
"A3 Building Plate"|"24"
"""

# DictWriter example
with open('items_dict.csv', 'w', newline='') as csvfile:
    fieldnames = ['Items', 'Price']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'Items': 'Workshop Kit', 'Price': '51'})
    writer.writerow({'Items': 'A3 Building Plate', 'Price': '24'})
