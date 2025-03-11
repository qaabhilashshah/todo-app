import csv


with open('app/weather.csv', 'r') as file:
    reader = list(csv.reader(file))

city = input('Enter city: ')

for row in reader[1:]:
    if row[0] == city:
        print(row[1])