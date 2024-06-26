import json, requests, datetime
current_date = datetime.date.today()
iso_calendar = current_date.isocalendar()

file = open('SECRET.json') # Opens the file

data = json.load(file) # loads the data then stores in variable called data

# Secret here:
secret = data['id']

# Database information here:
database = data['database_tasks']

file.close() # close file

url = 'https://api.notion.com/v1/pages'

# Headers
headers = {
    'Authorization': f'Bearer {secret}',
    'Content-Type': 'application/json',
    'Notion-Version': '2021-08-16'
}

#Get the workhours from the user
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
#Converts decimal hours to normal time
def convert_decimal_hours_to_time(decimal_hours):
    hours = int(decimal_hours)
    minutes = int((decimal_hours - hours) * 60)
    return hours, minutes

def main():
    week_number = iso_calendar[1]
    workedHours = get_worked_hours()
    print("\nWorked hours: ")
    workdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    total = 0
    for day, hour in zip(workdays, workedHours):
        print(f"{day}: {hour} hour")
        total += hour
    total_hours, total_minutes = convert_decimal_hours_to_time(total)
    total_time_str = f"{int(total_hours)}:{str(int(total_minutes)).zfill(2)}"
    sweek =str(week_number)
    print(f"Total time: {total_time_str}")
    print(f"The current week number is: {sweek}")

    # Data input
    data_input = {
       "parent": {"database_id": f"{database}"},
       "properties": {
           "Week": {
               "title": [
                {
                    "text": {
                        "content": f"{sweek}"
                    }
                }
            ]
        },
        "WorkHours": {
            "rich_text": [
                {
                    "text": {
                        "content": f"{total_time_str}"
                    }
                }
            ]
        }
    }
}

    # Check request
    response = requests.post(url, headers=headers, json=data_input)
    #print(response.json())

if __name__ == "__main__":
    main()