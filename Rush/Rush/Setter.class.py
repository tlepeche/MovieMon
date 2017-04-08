import random
import requests

def get_movies():
	myDict = dict()
	fd = open("/Users/tlepeche/projet/Pisc_Python/LocRush00_git/Rush/Rush/settings.txt")
	for line in fd:
		myDict.update({ (line[0 : line.index(':')]).strip() : (line[line.index(':') + 1 : len(line)]).strip() })
	fd.close()
	myList = myDict['id'].split(',')
	i = 0
	while i < len(myList):
		myList[i] = myList[i].strip()
		i += 1
	return myList



class Setter:
	data = dict()

	def __init__(self):
		random.seed()
		movies = get_movies()
		self.data = {
			'pos' : [5, 5],
			'balls' : 5,
		}
		i = 0
		list_movie = dict()
		while i < len(movies):
			list_movie.update({movies[i] : 'Uncatched' })
			i += 1
		self.data.update({'movies' : list_movie})
		rawData = dict()
		for keys in self.data['movies'].keys():
			payload = {'t' : keys}
			r = requests.get('http://www.omdbapi.com/?', params=payload)
			rawData.update({keys : r.text})
		self.data.update({'raw_data' : rawData})


	def load(self, game_file):
		pass

	def dump(self):
		pass

	def get_random_movie(self):
		choice = random.randint(0, len(self.data['movies']))
		for key in self.data['movies'].keys():
			if choice == 0:
				return key
			choice -= 1

	def load_default_settings(self):
		pass

	def get_strength(self):
		strenght = 0
		for values in self.data['movies'].values():
			if values == 'Catched':
				strenght += 1
		print(strenght)

	def get_movie(self, movieName):
		for keys in self.data['raw_data'].keys():
			if keys == movieName:
				return self.data['raw_data'][movieName]
		raise Exception("Data not found")

if __name__ == '__main__':
	test = Setter()
	test.get_strength()
	try:
		test.get_movie('The Matrix')
	except Exception as e:
		print(e)
	print(test.get_random_movie())
