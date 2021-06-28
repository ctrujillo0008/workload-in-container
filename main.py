from __future__ import print_function
import sys, warnings
import deepsecurity
from deepsecurity.rest import ApiException
from pprint import pprint
import csv
import pymsteams
import re



while(1):

	# Setup
	if not sys.warnoptions:
		warnings.simplefilter("ignore")
	configuration = deepsecurity.Configuration()
	configuration.host = 'https://cloudone.trendmicro.com/api'
	api_key=input("Enter your api_key")
	# Authentication
	configuration.api_key['api-secret-key'] = api_key

	# Initialization
	# Set Any Required Values
	api_instance = deepsecurity.ComputersApi(deepsecurity.ApiClient(configuration))
	api_version = 'v1'
	search_filter = deepsecurity.SearchFilter()
	expand_options = deepsecurity.Expand()
	expand_options.add(expand_options.none)
	expand = expand_options.list()
	overrides = False

	try:
		api_response = api_instance.search_computers(api_version, search_filter=search_filter, expand=expand, overrides=overrides)
		pprint(api_response)
	except ApiException as e:
		print("An exception occurred when calling ComputersApi.search_computers: %s\n" % e)

	api_response=str(api_response)
	#api_response=api_response.split(' ')
	with open("data.csv", "w",newline='') as csvfile:
		writer=csv.writer(csvfile,delimiter=",")
		api_response=list(api_response.split(","))
		#api_response=list(api_response.split(" " "))
		#spamwriter.writer
		# for element in list:
		# 	writer.writerow([element])
		# for item in csvfile:
		# 	csvfile.write(api_response.replace(",",""))
		writer.writerow(api_response)

		#API RESPONSE IS A LIST
	#myTeamsMessage = pymsteams.connectorcard("https://trendmicro.webhook.office.com/webhookb2/3bbd7e54-4acd-49b5-9fca-55e3335d6f47@3e04753a-ae5b-42d4-a86d-d6f05460f9e4/IncomingWebhook/980609c7cc874a3c99025749f0b2c852/d6f41048-b13b-41f1-8ced-e30d761668b1")
	#cat=print(*api_response)

	myTeamsMessage = pymsteams.connectorcard("https://trendmicro.webhook.office.com/webhookb2/3bbd7e54-4acd-49b5-9fca-55e3335d6f47@3e04753a-ae5b-42d4-a86d-d6f05460f9e4/IncomingWebhook/980609c7cc874a3c99025749f0b2c852/d6f41048-b13b-41f1-8ced-e30d761668b1")

	#IMPORTANT
	for i in api_response:
		myTeamsMessage.text(i)
		myTeamsMessage.send()



	#	if(api_response[i]=='platform: ''')

	# def convert(s):
	# 	str1=" "
	# 	return(str1.join(s))



	# for i in api_response:
		



	# print('STARTS HERE')
	# cat=type(api_response)#IS A LIST CLASS 'LIST'
	# print(cat)
	#print api_response.rsplit('\n',1)[0]
	# cat=api_response.pop(50)


			
		
	# print(cat)
