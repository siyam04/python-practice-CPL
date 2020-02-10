import csv
from pprint import pprint


with open('FL_insurance_sample.csv', 'r') as csv_file:
    # reader = csv.reader(csv_file, skipinitialspace=True)
    reader = csv.reader(csv_file, skipinitialspace=True)

    for row in reader:
        # pprint(row)
        print(row)



