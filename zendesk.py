from dotenv import load_dotenv
import requests
import os
import csv

load_dotenv()

SUBDOMAIN = os.getenv('SUBDOMAIN')
EMAIL = os.getenv('EMAIL')
PASSWORD = os.getenv('PASSWORD')

zendesk_uri = 'https://' + SUBDOMAIN + '.zendesk.com/api/v2/users.json'
response = requests.get(zendesk_uri, auth=(EMAIL, PASSWORD))

if response.status_code == 200:
    data = response.json()
    with open('generated_csv/user-list.csv', mode='w') as csv_file:
        fieldnames = ['id', 'name']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for user in data['users']:
            print(str(user['id']) + '  ' + user['name'])
            writer.writerow({'id': str(user['id']), 'name': user['name']})
else:
    print('Request failed')
    print(response.status_code)

