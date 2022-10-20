import requests
import os
import json
from time import sleep
try:
  sleep (2)
  print ("\033[1;32;40mshamia's ip tracker")
  ip_tracker = input('\033[4;32;45menter an ip address= ')
  api = 'http://ip-api.com/json/'
  res = requests.get(api + ip_tracker)
  data = res.json()
  os.system('clear')
  sleep (0.5)
  print (f"""\033[1;31;47m
  ip: {data['query']}
  status: {data['status']}""")
  sleep (1)
  print (f"""\033[1;31;47m
  country: {data['country']}
  countryCode: {data['countryCode']}
  region: {data['region']}
  regionName: {data['regionName']}
  city: {data['city']}
  zip: {data['zip']}
  lat: {data['lat']}
  lon: {data['lon']}
  timezone: {data['timezone']}""")
  sleep (1)
  print (f"""\033[1;31;47m
  isp: {data['isp']}
  org: {data['org']}
  as: {data['as']}
  """) 
except:  
    print ("invalid ip address!.")
