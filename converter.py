from datetime import datetime, timezone
import json, requests

file = open("SECRET.json")


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
    total_hours, total_minutes = convert_decimal_hours_to_time(total)
    print("Weekly Total: ",total_hours,":", total_minutes)        

def convert_decimal_hours_to_time(decimal_hours):
    hours = int(decimal_hours)
    minutes = int((decimal_hours - hours) * 60)
    return hours, minutes


    
if __name__ == "__main__":
    main()


#TODO: add database connection to save weekly hours
