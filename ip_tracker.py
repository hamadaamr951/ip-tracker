#!/bin/python3
import requests
import os
import json
from time import sleep
import socket
def dox():
    try:
      os.system('clear')
      print ("\033[1;36;41m`•.¸¸.•´´¯`••._.• cＯ𝐫𝕖 •._.••`¯´´•.¸¸.•`")
      i = input("do you want to get info of this machine and the target ip?: ")
      if i == yes:
          hostname = socket.gethostname()
          localip = socket.gethostbyname(hostname)
          sleep (2)
          ip_tracker = input('\033[1;32;40menter an ip address= ')
          api = 'http://ip-api.com/json/'
          res = requests.get(api + ip_tracker)
          data = res.json()
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
          current host: + {hostname}
          local ip for this machine: + {localip}""")
      elif i == no:
          print ('gtfo!')
    except:
        print ("invalid input dumbass!.")
dox()
