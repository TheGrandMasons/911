import csv
from DataSet import *
from Functions import *

# with open('reporthistory.csv', 'r') as csvfile:
#         reader = csv.DictReader(csvfile)
#         incList = []
#         # Iterate through each row in the CSV file
#         for row in reader:
#             # Append the value from the specified column to the list
#             incList.append(row['ssn'])    
#         print (incList)

# with open('capture.csv', 'w') as demo:
#     for ssn in pList:
#         demo.write(f'{genPhone()},{random.choice(nature_and_severity)},{ssn},{random.choice(range(10000, 10400))}\n')

with open('ers.csv', 'w') as demo:
    for num in incList:
        demo.write(f'{num},{random.choice(dispatched_units)},{random.choice(law_enforcement)},{random.choice(other_first_responders)}\n')