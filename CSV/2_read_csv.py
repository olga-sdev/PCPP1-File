import csv

with open('items.csv', newline='') as csvfile:
    """
    csv.reader() method with parameters file and delimiters
    """
    reader = csv.reader(csvfile, delimiter='|')
    for row in reader:
      print(': '.join(row))
        

"""
Item: Price
Soldering-Kit-220V: 37
IoTerrific-Bundle: 90
PLC-Starter-Kit: 431
Voice-Controlled-Light-Bundle: 61
"""


with open('items.csv', newline='') as csvfile:
    """
    csv.DictReader() method with parameters file, delimeter and fileldnames
    """
    fieldnames = ['Item', 'Price']
    reader = csv.DictReader(csvfile, delimiter='|', fieldnames=fieldnames)
    for row in reader:
        print(row['Item'], '-', row['Price'])


"""
Item - Price
Soldering-Kit-220V - 37
IoTerrific-Bundle - 90
PLC-Starter-Kit - 431
Voice-Controlled-Light-Bundle - 61
"""
