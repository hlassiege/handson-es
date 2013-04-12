import requests, json

BASE_PATH = "http://localhost:9200/library/movie"

print "\n\n\tSearch Django in every field of the document"

r = requests.get(BASE_PATH+"/_search?q=Django")
print r.text


print "\n\n\tSearch New York in title field of the document"

r = requests.get(BASE_PATH+"/_search?q=title:New%20York")
print r.text


print "\n\n\tSearch new york in title field of the document"

r = requests.get(BASE_PATH+"/_search?q=title:new%20york")
print r.text


print "\n\n\tSearch new yark in title field of the document"

r = requests.get(BASE_PATH+"/_search?q=title:new%20yark")
print r.text


print "\n\n\tSearch Manhattan in filming_locations field of the document"
r = requests.post(BASE_PATH+"/_search?q=filming_locations:Manhattan")
print r.text


print "\n\n\tFuzzy Search Manhattan in filming_locations field of the document"

data = {"query" : { "fuzzy" : { "filming_locations" : "Manhattan" }}}

r = requests.post(BASE_PATH+"/_search", data=json.dumps(data))
print r.text