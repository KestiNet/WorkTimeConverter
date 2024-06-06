import json, requests

file = open("SECRET.json")

data = json.load(file)

#Secret token
secret = data['id']

#database id
database = data['database']
file.close()

#url
url = 'https://api.notion.com/v1/pages'

#headers
headers = {
    'Authorization': f'Bearer {secret}',
    'Content-Type':'application/json',
    'Notion-Version': '2022-06-28'
}

#Data input
data_input = {
	"parent": { "page_id": "e43c0844-db01-4e08-8d1f-01fcbbd52764" },
	"properties": {
		"title": {
      "title": [{ "type": "text", "text": { "content": "A note from your pals at Notion" } }]
		}
	},
	"children": [
    {
      "object": "block",
      "type": "paragraph",
      "paragraph": {
        "rich_text": [{ "type": "text", "text": { "content": "You made this page using the Notion API. Pretty cool, huh? We hope you enjoy building with us." } }]
      }
    }
  ]
}
#Check request

response = requests.post(url, headers=headers,json=data_input)
print(response.json())
'''
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


#TODO: need to create conversion from decimal hours to normal hours
#TODO: add database connection to save weekly hours


'''