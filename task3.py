import requests
import json
def geticket():
    url = "https://sandboxapicem.cisco.com/api/v1/ticket"
    data = {}
    data["username"] = "devnetuser"
    data["password"] = "Cisco123!"
    data = json.dumps(data)
    headers = {'Content-type': 'application/json'}
    response = requests.post(url, data=data,headers=headers)
    print(response.json()['response']['serviceTicket'])

geticket()# to complete task 3 of open book

def getNetworkData():
    token = GetToken()
    print(token)
    url = "https://sandboxapicem.cisco.com/api/v1/host"
    headers = {'Content-type': 'application/json','X-Auth-Token':token}
    response = requests.get(url,headers=headers,verify=False)
    response =  response.json()['response']
    for r in response:
        print(r)

getNetworkData()
