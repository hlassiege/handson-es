import requests, json

BASE_PATH = "http://localhost:9200/"


r = requests.delete(BASE_PATH+"/library/movie/")

r = requests.get(BASE_PATH+"/library/movie/_count")
print "Number of document in the index : %s" % r.json()['count']