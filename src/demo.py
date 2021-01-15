import csv
with open('dataset/hypothesis_analises.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
