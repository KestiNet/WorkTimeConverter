from datetime import datetime, timezone
import json, requests

<<<<<<< HEAD
file = open("SECRET.json")
=======
NOTION_TOKEN = 
DATABASE_ID = "0c82028703674810a06e36a3ccb1b4b4"
>>>>>>> origin/main

data = json.load(file)

#Secret token
secret = data['id']

#database id
database = data['database']
file.close()

#url
url_create = "https://api.notion.com/v1/pages"



#headers
headers = {
    "Authorization": "Bearer " + secret,
    "Content-Type":"application/json",
    "Notion-Version": "2022-06-28"
}


def get_worked_hours():

    workdays = ['Monday', 'Tuesday', 'Wednesday','Thursday', 'Friday']
    hoursWorked = []
    for days in workdays:
        enteredHours = float(input(f"Enter worked hours for {days}: "))
        if enteredHours < 0:
            print("Cant enter negative numbers")
            continue
        hoursWorked.append(enteredHours)

    return hoursWorked

def main():
    workedHours = get_worked_hours()
    print("\nWorked hours: ")
    workdays = ['Monday', 'Tuesday', 'Wednesday','Thursday', 'Friday']
    total = 0
    for day, hour in zip(workdays,workedHours):
        print(f"{day}: {hour} hour")
        total += hour
    print("Weekly total: ", total)
        

    


    
if __name__ == "__main__":
    main()


#TODO: need to create conversion from decimal hours to normal hours
#TODO: add database connection to save weekly hours


<<<<<<< HEAD
=======
'''
>>>>>>> origin/main
