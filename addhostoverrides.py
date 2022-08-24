#! /usr/bin/python3

import requests
import json
import csv
import time

# API Document  - https://docs.opnsense.org/development/api.html#introduction
# API Reference for Unbound - https://docs.opnsense.org/development/api/core/unbound.html


# Note:  The user must be in the admin group

api_key = 'Your API Key'
api_secret = 'Your API Secret'
host = 'https://Your_Firewall'

domain = "TestDomain.com"


csv_file = "something.csv"


url = host + '/api/unbound/settings/AddHostOverride'



with open(csv_file, mode ='r')as file:
   
  # reading the CSV file
  csvFile = csv.reader(file)
 
  # displaying the contents of the CSV file
  for line in csvFile:
        # print(line[0])

        hostname    = line[1]
        domain      = domain
        ip_address  = line[0]
        description = ""


        # You can set other properties if you need to.
        # Look at https://github.com/opnsense/core/blob/master/src/opnsense/mvc/app/models/OPNsense/Unbound/Unbound.xml
        # or execute a GET from /api/unbound/settings/get
      
        payload = json.dumps({
        "host": {
            "enabled": "1",
            "hostname": hostname,
            "domain": domain,
            "server": ip_address,
            "description": description
        }
        })
        headers = {
        'Content-Type': 'application/json',
        }

        response = requests.request("POST", url, auth=(api_key, api_secret), headers=headers, data=payload)

        print(hostname + ' @ ' + ip_address + ' || ' + response.text)
        #print(hostname + ' @ ' + ip_address)
        
        # wait a 1/2 second so we don't overload the firewall.... JUST IN CASE 
        time.sleep(0.6)     
