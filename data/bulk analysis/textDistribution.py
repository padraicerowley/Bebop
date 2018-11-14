import nltk
import json

with open('C:/Users/116/Desktop/development/bebop/data/veniceflooding.json',encoding="utf8") as data_file:
    data = json.dumps(json.load(data_file))

    for tweet in data['tweets']:
        print (str(tweet['parseTags']))