#!/usr/bin/python

# Written by Peter Entwistle

import os
import requests
from bs4 import BeautifulSoup as BS
path = os.path.dirname(os.path.abspath(__file__))+'/ip'

# Set your details
username = 'youremail@example.com'
password = 'yourPassword'
hostname = 'yourDnsDynamicSubDomain'

def getIp():
	'''Gets the current external ip address'''
	url = 'http://myip.dnsdynamic.org'
	r = requests.get(url)
	ip = BS(r.text)
	return str(ip)

def checkLastIp():
	'''Checks the last ip address'''
	f = open(path, 'r')
	lastIp = f.readline()
	f.close()
	return str(lastIp)

def writeIp(ip):
	'''Writes the new ip to the file'''
	f = open(path, 'w')
	f.write(ip)
	f.close()

def sendIp(ip,username,password):
	'''Send the new ip to dnsdynamic'''
	payload = {'hostname': hostname, 'myip': ip}
	r = requests.get("https://"+username+":"+password+"@www.dnsdynamic.org/api/", params=payload)
	response = BS(r.text)
	return str(response)

# Check if the ip file exists
if not os.path.isfile(path):
	ip = getIp()
	writeIp(ip)
	sendIp(ip,username,password)
	print "Created ip file and updated the IP"
else:
	currentIp = getIp()
	lastIp = checkLastIp()
	if currentIp != lastIp:
		# The current ip is different so need to update
		writeIp(currentIp)
		response = sendIp(currentIp,username,password)
		print "Sent new IP"
	else:
		print "IP is the same no need to update"