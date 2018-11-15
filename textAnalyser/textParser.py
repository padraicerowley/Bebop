import csv
import re
import nltk
import json
import time
start = time.time()
end = time.time()
print(end - start)

class parseWriter():
    found_msg_path = 'C:/Users/116/Desktop/development/bebop/data/tweets'
    verbTablePath = 'C:/Users/116/Desktop/development/bebop/data/italian/verbs.csv'
    nounTablePath = 'C:/Users/116/Desktop/development/bebop/data/italian/nouns.csv'
    userTablePath = 'C:/Users/116/Desktop/development/bebop/data/italian/users.csv'
    blockCount = 1

    fob = open(
        found_msg_path+ str(time.ctime().replace(" ", "_").replace(":","")) +'.json',
        'wb')
    output = {"tweets": []}


    def newBlock(self,tweetText,date,fv,rt):
        self.fob.write(str(self.output).encode('utf-8'))
        self.fob.close()
        print("new block:" + str(time.ctime()))
        self.blockCount +=1
        self.fob = open(
            self.found_msg_path + str(time.ctime())+'.json',
            'wb')
        self.output = {"tweets": []}
        self.addTweet(tweetText,date,fv,rt)



    def addTweet(self,tweetText,date,fv,rt):
        urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',
                          tweetText)
        rawTweet = tweetText
        for url in urls:
            tweetText = tweetText.replace(url, "WEBSITE")
        text = nltk.word_tokenize(tweetText)
        taggedTweet = nltk.pos_tag(text)
        self.updateNouns(taggedTweet)
        #self.updateVerbs(taggedTweet)
        #self.updateUsers(taggedTweet)
        tweet = {}
        tweet["text"] = str(rawTweet)
        tweet["language"] = "it"
        tweet["time"] = str(date)
        tweet["urls"] = str(urls)
        tweet["fav"] = fv
        tweet["retweets"]= rt
        tweet["parseTags"] = str(taggedTweet)
        self.output["tweets"].append(tweet)
        print(json.dumps(tweet))

    def updateNouns(self,text):
        nounFile = open(self.nounTablePath,encoding='utf-8')
        nounTable = csv.reader(nounFile)
        nouns = list(nounTable)
        nounFile.close()
        print("----------------------------------")
        print(text)
        for tag in text:
            alreadyFound= False
            if(tag[1] == "NNP"):
                for noun in nouns:

                    if(noun[0]==tag[0]):
                        noun= [tag[0],int(noun[1]) + 1]
                        alreadyFound=True
                        print("update: " + noun[0])

                if(alreadyFound==False):
                    nouns.append((tag[0], 1))
                    print("new: " + tag[0])

        writer = csv.writer(open(self.nounTablePath,'w',newline='',encoding='utf-8'))
        writer.writerows(nouns)

    def updateUsers(self,user):
        userTable = csv.reader(open(self.userTablePath))
        users = list(userTable)

        writer = csv.writer(open(self.userTablePath, 'w'))
        writer.writerows(users)



    def updateVerbs(self,text):
        verbTable = csv.reader(open(self.verbTablePath))
        verbs = list(verbTable)

        writer = csv.writer(open(self.verbTablePath, 'w'))
        writer.writerows(verbs)
