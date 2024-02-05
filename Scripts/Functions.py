import random
from DataSet import *

#This code defines a function called address that generates a random address. It selects a city randomly (1, 2, or 3), then generates a random number between 1 and 120, and selects a street based on the city.
def genAddress():
        citySelector = random.randint(1,3)
        if citySelector == 1:
            tempAddress = f'{random.randrange(1, 120)} {random.choice(cairo_streets)}'
        elif citySelector == 2:
            tempAddress = f'{random.randrange(1, 120)} {random.choice(giza_streets)}'
        elif citySelector == 3:
            tempAddress = -'{random.randrange(1, 120)} {random.choice(alexandria_streets)}'
        return tempAddress

#This code defines a function called name() that randomly selects a first name, middle name, and last name. It also determines the sex of the person based on a randomly generated number
def genName():
    sexSelector = random.randint(1, 2)
    if sexSelector == 1:
        tempFirstName = random.choice(maleName)
        tempMiddleName = random.choice(maleName)
        tempLastName = random.choice(maleName)
        tempSex = "M"
        name = f'{tempFirstName} {tempMiddleName} {tempLastName}'
    elif sexSelector == 2:
        tempFirstName = random.choice(femaleName)
        tempMiddleName = random.choice(maleName)
        tempLastName = random.choice(maleName)
        tempSex = "F"
        name = f'{tempFirstName} {tempMiddleName} {tempLastName}'
    return tempFirstName, tempMiddleName, tempLastName, name, tempSex

def genID():
    tempMonth = random.randrange(1, 12)
    if tempMonth == 2:
        tempDay = random.randrange(1, 28)
    elif tempMonth in [1, 3, 5, 7, 8, 10, 12]:
        tempDay = random.randrange(1, 31)
    elif tempMonth in [4, 6, 9, 11]:
        tempDay = random.randrange(1, 30)
    
    if tempDay < 10:
        tempDay = f'0{tempDay}'
    if tempMonth < 10:
        tempMonth = f'0{tempMonth}'
    genSelector = random.randint(0, 1)
    if genSelector == 0:
        y = random.randrange(30, 99)
        tempBirthYear = int(f'19{y}')
        tempNationalID = f'2{tempBirthYear}{tempMonth}{tempDay}{random.randint(1000000, 9999999)}'
        tempBirthDate = f'{tempBirthYear}-{tempMonth}-{tempDay}'
    elif genSelector == 1:
        y = random.randrange(00, 23)
        if y < 10:
            tempBirthYear = int(f'200{y}')
            tempNationalID = f'30{y}{tempMonth}{tempDay}{random.randint(1000000, 9999999)}'
            tempBirthDate = f'{tempBirthYear}-{tempMonth}-{tempDay}'
        else:
            tempBirthYear = int(f'20{y}')
            tempNationalID = f'3{y}{tempMonth}{tempDay}{random.randint(1000000, 9999999)}'
            tempBirthDate = f'{tempBirthYear}-{tempMonth}-{tempDay}'
    return tempNationalID, tempBirthYear, tempMonth, tempDay, tempBirthDate

def genPhone():
    tempPhone =f'013{random.randint(10000000, 99999999)}'
    return tempPhone