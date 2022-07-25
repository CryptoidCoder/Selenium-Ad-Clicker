import myst


# options for Country: US, FR, DE, AU, GB, SE, etc.
# options for Type: hosting or residential
# datacenters are obviously faster but many websites will block their ip's
myst.new_connection(Country='US', Type='residential')


import requests
import json

def get():
    endpoint = 'https://ipinfo.io/json'
    response = requests.get(endpoint, verify = True)

    if response.status_code != 200:
        return 'Status:', response.status_code, 'Problem with the request. Exiting.'
        exit()

    data = response.json()

    return data['ip']

#get my ip
my_ip = get()

#print my ip
print(my_ip)
