import requests, json

BASE_PATH = "http://localhost:9200/library/movie"

print "\n\n\tSearch Django in every field of the document"

data = {"query" : { "match" : { "_all" : "Django" }}}
r = requests.post(BASE_PATH+"/_search", data=json.dumps(data))
print r.text


print "\n\n\tSearch York in filming_locations field of the document"

data = {"query" : { "match" : { "filming_locations" : "York" }}}
r = requests.post(BASE_PATH+"/_search", data=json.dumps(data))
print r.text


print "\n\n\tSearch york in filming_locations field of the document"

data = {"query" : { "match" : { "filming_locations" : "york" }}}
r = requests.post(BASE_PATH+"/_search", data=json.dumps(data))
print r.text


print "\n\n\tSearch yark in filming_locations field of the document"
data = {"query" : { "match" : { "filming_locations" : "yark" }}}
r = requests.post(BASE_PATH+"/_search", data=json.dumps(data))
print r.text


print "\n\n\tSearch Manhattan in filming_locations field of the document"
data = {"query" : { "match" : { "filming_locations" : "Manhattan" }}}
r = requests.post(BASE_PATH+"/_search", data=json.dumps(data))
print r.text


print "\n\n\tFuzzy Search Manhattan in filming_locations field of the document"

data = {"query" : { "fuzzy" : { "filming_locations" : "Manhattan" }}}
r = requests.post(BASE_PATH+"/_search", data=json.dumps(data))
print r.text