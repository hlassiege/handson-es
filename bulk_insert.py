import requests, json

BASE_PATH = "http://localhost:9200/"

f = open('movies.json', 'r')
data = json.load(f)
f.close()

for movie in data:
	r = requests.post(BASE_PATH+"/library/movie/"+movie['imdb_id'], data=json.dumps(movie))


r = requests.get(BASE_PATH+"/library/movie/_count")
print "Number of document in the index : %s" % r.json()['count']