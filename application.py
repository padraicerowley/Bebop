from flask import Flask
from flask import Response
import json
import pprint
import webController.textCalls as textCall

# Test page text
header_text = '''
    <html>\n<head> <title>Haystack</title> </head>\n<body>'''
instructions = '''
    <p><em>Hint</em>: This is the Haystack API. We hope you will find your needle in here!</p>\n'''
home_link = '<p><a href="/">Back</a></p>\n'
footer_text = '</body>\n</html>'

# EB looks for an 'application' callable by default.
application = Flask(__name__)

# test its live.
application.add_url_rule('/', 'index', (lambda: header_text + instructions + footer_text))


#------------------------------------TEXT-----------------------------------------------

#text analytics live
@application.route('/getTweetStream/<lang>', methods=['GET', 'POST'])
def getLiveStream(lang):
    results = textCall.getStream(lang)
    r = Response(response=results, status=200, mimetype="application/xml")
    r.headers["Content-Type"] = "application; charset=utf-8"
    r.headers['Access-Control-Allow-Origin'] = '*'
    return r


#@application.route('/searchTwitter/<term>', methods=['GET', 'POST'])
def getLiveStream(term):
    results = textCall.getLiveData(term)
    r = Response(response=results, status=200, mimetype="application/xml")
    r.headers["Content-Type"] = "application; charset=utf-8"
    r.headers['Access-Control-Allow-Origin'] = '*'
    return r


# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = False
    application.run()