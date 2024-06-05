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

    for day, hour in zip(workdays,workedHours):
        print(f"{day}: {hour} hour")
    
if __name__ == "__main__":
    main()





