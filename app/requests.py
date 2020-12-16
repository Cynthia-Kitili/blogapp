import urllib.request,json
from .models import Quote

base_url = None
def configure_request(app):
    global base_url
    base_url = app.config['QUOTE_API_BASE_URL']
def getQuotes():
    getQuotes_url = 'http://quotes.stormconsultancy.co.uk/random.json'
    with urllib.request.urlopen(getQuotes_url) as url:
        getQuotes_data = url.read
        quotesResponse = url.read()
        word = json.loads(quotesResponse)
        print(word)
        read = []
        id = word.get('id')
        author = word.get('author')
        quote = word.get('quote')
        quoteObject = Quote(id,author,quote)
        read.append(quoteObject)
    return read 
    