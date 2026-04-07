import json
import csv


with open('/Users/ASUS/data.json', 'r') as json_file:
        data = json.load(json_file)

with open('output.csv', 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['name', 'age', 'city'])
        for item in data:
            writer.writerow([item['name'], item['age'], item['city']])

print("Data has been successfully converted from JSON to CSV.")