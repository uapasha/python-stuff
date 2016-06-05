

from sys import argv
from json import loads
######## CONSTANTS ################
TOP_RESPONSES = 5
TOP_PAGES = 5
######## Global Variables #########
## dictionaries for keeping data for domain statistics
popular_pages = {}
biggest_responses = {}
IPs = {}

###### Helper functions ###########
def parse_HTTPRequest(HTTPRequest):
	sourse, http, other = HTTPRequest[5:].partition(' HTTP')
	return sourse

def top_pages(popular_pages, domain):
	return sorted(popular_pages[d], key = list().count, 
									reverse = True)[:TOP_PAGES]

###### Process flow #################
## declare a list with all files that need to be opened
files = argv[1:]

for f in files:
	with open(f, 'r') as json:
		data_list = loads(json.read())

		for data in data_list:
			## define domain name without regard to WWW
			domain = data['domain'].replace('www.', '')

			### keep track of popular pages

			## initialize dictionary key with particular domain
			## if not created
			if domain not in popular_pages.keys():
				popular_pages[domain] = []

			## parse source page from http request
			page = parse_HTTPRequest(data['HTTPRequest'])

 			### keep track of responses size

			## initialize dictionary key with particular domain
			## if not created for keeping responces
			if domain not in biggest_responses.keys():
				biggest_responses[domain] = []

			## list for keeping TOP_RESPONSES of particular domain  
			responses_list = biggest_responses[domain]

			## split response into status and response size
			## keep only response size
			response_size = int(data['responseStatus'].split()[1])

			if responses_list == []:
				responses_list.append(response_size)

			elif response_size > min(responses_list):
				responses_list.append(response_size)

				if len(responses_list) > TOP_RESPONSES:
					biggest_responses[domain].remove(min(responses_list))

			### keep track of unique IPs

			## initialize dictionary key with particular domain
			## if not created for keeping IPs in the form of set
			if domain not in IPs.keys():
				IPs[domain] = set()

			## add uniqe IP to the set of IPs of particular domain
			IPs[domain].update([data['IP']])
	json.close()



#### printing results ##########

for d in popular_pages:
	print("----------------------")
	print ("--domain is: ")
	print (" %s" % d)
	print ("most popular pages are: ")
	if (top_pages(popular_pages, d) != []):
		for p in top_five_pages(popular_pages, d):
			print (" " + p)
	else:
		print('-Home Directory: %s' % d)
	print ('biggest responses are: ')
	for r in (sorted(biggest_responses[d], reverse = True)):
		print (" " + str(r))
	print ('total unique hosts: ')
	print (" " + str(len(IPs[d])))