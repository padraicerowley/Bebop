import webController.services.twitterRequests as textRequester



def getStream(lang):
    tweets=textRequester.getTwitterStream(lang)

def getLiveData(word):
    tweets = textRequester.getTwitterData(word)
    return  tweets