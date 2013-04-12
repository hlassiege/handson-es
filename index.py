import requests, json

BASE_PATH = "http://localhost:9200/"

f = open('movies.json', 'r')
data = json.load(f)
f.close()

movie = data[0]

print "Indexing movie %s ...\r\n" % movie

r = requests.post(BASE_PATH+"/library/movie", data=json.dumps(movie))
print r.text


r = requests.get(BASE_PATH+"/library/movie/_count")
print "Number of document in the index : %s" % r.json()['count']