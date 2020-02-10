import csv
from pprint import pprint


with open('FL_insurance_sample.csv', 'r') as csv_file:
    # reader = csv.reader(csv_file, delimiter='|')
    # reader = csv.reader(csv_file, skipinitialspace=True)
    dict_reader = csv.DictReader(csv_file)

    for row in dict_reader:
        print(dict(row))

    # for row in reader:
        # pprint(row)
        # print(row)



