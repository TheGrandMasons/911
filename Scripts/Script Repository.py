import csv
from DataSet import *
from Functions import *

# SSN Colector
with open('demographic.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        ssnList = []
        # Iterate through each row in the CSV file
        for row in reader:
            # Append the value from the specified column to the list
            ssnList.append(row['ssn'])    
        print (ssnList)

# Demographic Insertor
with open('demographic.csv', 'w') as demo:
    ssnList = []
    for x in range(1, 601):
        ssn, birthYear, birthMonth, birthDay, birthDate = genID()
        fName, mName, lName, name, sex = genName()
        address = genAddress()
        contact = genPhone()
        if ssn not in ssnList:
            ssnList.append(ssn)
            demo.write(f'{ssn},{name},{birthDate},{address},{sex},{contact},{random.choice(insuranceProviders)}\n')

# Allergies Insertor
with open('allergies.csv', 'w') as demo:
    for ssn in ssnList:
        demo.write(f'{ssn},{random.choice(allergies)},{random.choice(intolerances)},{random.choice(adverse_reactions_to_medication)}\n')

# Provider Insertor
with open('provider.csv', 'w') as demo:
    for name in nameList:
        ssn = int(ssnList[nameList.index(name)])
        if ssn not in range(30000000000000, 40000000000000):
            demo.write(f'{ssn},{name}\n')

# Prescriptions Insertor
with open('prescriptions.csv', 'w') as demo:
    for ssn in ssnList:
        demo.write(f'{ssn},{random.choice(providers)},{random.choice(medications)} {random.choice(dosages)},{random.choice(random_dates_list)},{random.choice(medication_warnings)} & {random.choice(medication_warnings)} & {random.choice(medication_warnings)}\n')

# Firefighters Insertor
firefighters = []
for ssn in ssnList:
    if ssn  in providers and int(ssn) not in range(30000000000000, 40000000000000):
        firefighters.append(ssn)
print (firefighters)

# Firereport Insertor
with open('firereports.csv', 'w') as demo:
    for num in range(1000, 1017):
        random.choice(ssnList)
        demo.write(f'{random.choice(ssnList)},{num},{random.choice(random_dates_list)}\n')

# History Insertor
with open('visits.csv', 'w') as demo:
    for ssn in ssnList:
        demo.write(f'{ssn},{random.choice(chronic_conditions_list)},{random.choice(past_treatments_list)},{random.choice(surgeries_list)},{random.choice(hospitalizations_list)},{random.choice(immunizations_list)}\n')

# Visits Insertor
with open('visits.csv', 'w') as demo:
    for ssn in ssnList:
        demo.write(f'{ssn},{random.choice(details_list)},{random.choice(symptoms_list)},{random.choice(diagnoses_list)},{random.choice(treatments_list)},{random.choice(procedures_list)},{random.choice(lab_results_list)}\n')

# Locations Insertor
with open('log.csv', 'w') as demo:
    for ssn in ssnList:
        demo.write(f'{random.choice(alexandria_streets)}\n')

# 101631, 101897