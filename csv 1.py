# csv reader

import csv

# -----------------------------------------------------------
with open('input Jeremy sector forecasts 2015_10_2.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        print row
