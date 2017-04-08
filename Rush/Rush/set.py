import requests
import json

def load_settings():
	myDict = dict()
	fd = open("/Users/tlepeche/projet/Pisc_Python/LocRush00_git/Rush/Rush/settings.txt")
	fd2 = open("/Users/tlepeche/projet/Pisc_Python/LocRush00_git/Rush/Rush/VERIF", 'w')
	for line in fd:
		myDict.update({ (line[0 : line.index(':')]).strip() : (line[line.index(':') + 1 : len(line)]).strip() })
	fd.close()
	reqAPI(myDict, fd2)

def reqAPI(myDict, fd):
	myList = myDict['id'].split(',')
	i = 0
	while i < len(myList):
		payload = {'t' : myList[i].strip()}
		r = requests.get('http://www.omdbapi.com/?', params=payload)
		j = json.loads(r.text)
		fd.write(j['Title'])
		fd.write(' : ')
		var = j['Ratings'][0]['Value']
		#Movie Rating
		rating = var[0 : var.index('/')]
		fd.write(rating)
		fd.write('\n')
		i += 1
	fd.close()
