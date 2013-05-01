import requests, json

BASE_PATH = "http://localhost:9200/library/movie"

print "\n\n\tSearch English with a boost on plot_simple field of the document"


data = {"from" : 0, "size" : 1,
		"query":{
		"bool" : {
		"should" : [ {
		  "match" : {
			"plot_simple" : {
			  "query" : "English",
			  "boost" : -1.5
			}
		  }
		}, {
		  "match" : {
			"language" : {
			  "query" : "English",
			  "boost" : 1.0
			}
		  }
		} ]
	  }
	}
  }
r = requests.post(BASE_PATH+"/_search", data=json.dumps(data))
print r.text


print "\n\n\tSearch English with a custom score computed on rating"
data = {"from" : 0, "size" : 1,
	"query" : {
      "custom_score" : {
        "query" : {
              "match" : {
                "language" : "English"
                }
              },
			  "script" : "_score + ( doc['rating_count'].value > 36000 ? doc['rating'].value : 0 )"
        }
      }
    }

r = requests.post(BASE_PATH+"/_search", data=json.dumps(data))
print r.text

print "\n\n\tMatch all sorted by rating"
data = { "from" : 0, "size" : 1,
	     "sort" : [ { "rating" : {"order" : "desc"} } ],
		 "query" :{ "match_all" : { }}
	   }

r = requests.post(BASE_PATH+"/_search", data=json.dumps(data))
print r.text



print "\n\n\tMatch all in range of rating 0-7"
data =  {"from" : 0, "size" : 1,
    "filter" : {
            "range" : {
                "rating" : { 
                    "from" : "0", 
                    "to" : "8.1", 
                    "include_lower" : 'true', 
                    "include_upper" : 'false'
                }
            }
        }
    }

r = requests.post(BASE_PATH+"/_search", data=json.dumps(data))
print r.text
