import json, requests
from datetime import datetime


file = open("SECRET.json")

data = json.load(file)

#Secret token
secret = data['id']

#database id
database = data['database']
file.close()

#url
#url = 'https://api.notion.com/v1/pages'

#headers
headers = {
    'Authorization': f'Bearer {secret}',
    'Content-Type':'application/json',
    'Notion-Version': '2022-06-28'
}

def get_pages():
    url = f"https://api.notion.com/v1/databases/{database}/query"
    payload = {"page_size":100}
    response = requests.post(url, json=payload, headers=headers)
    data = response.json()
    
    with open('db.json', 'w', encoding='utf8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    results = data["results"]
    return results

pages = get_pages()
for page in pages:
    page_id = page["id"]
    props = page["properties"]
    url = props["URL"]["title"][0]["text"]["content"]
    title = props["Title"]["rich_text"][0]["text"]["content"]
    published = props["published"]["date"]["start"]
    published = datetime.fromisoformat(published)
    print(url, title, published)


'''
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
'''
#Check request
'''
response = requests.post(url, headers=headers,json=data_input)
print(response.json())

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