def load_settings():
	myDict = dict()
	fd = open("/Users/tlepeche/projet/Pisc_Python/LocRush00/Rush/MovieMon/settings.txt")
	fd2 = open("/Users/tlepeche/projet/Pisc_Python/LocRush00/Rush/MovieMon/VERIF", 'w')
	for line in fd:
		myDict.update({line[0 : line.index(':')] : line[line.index(':') + 1 : len(line)]})
	for key, value in myDict.items():
		string = key + ' ->' + value
		fd2.write(string)
	fd2.close()
	fd.close()


