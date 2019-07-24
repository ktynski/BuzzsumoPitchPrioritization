thelist = ('bbc.co.uk',
'businessinsider.com',
'cnbc.com',
'cnn.com',
'engadget.com',
'entrepreneur.com',
'forbes.com',
'gizmodo.com',
'hbr.org',
'iflscience.com',
'independent.co.uk',
'linkedin.com',
'mashable.com',
'medium.com',
'money.cnn.com',
'nytimes.com',
'qz.com',
'sciencemag.org',
'scmp.com',
'techcrunch.com',
'theatlantic.com',
'theguardian.com',
'thenextweb.com',
'theverge.com',
'venturebeat.com',
'washingtonpost.com',
'wired.com',
'wsj.com')





def getarticleshares(domain):
    url = "https://api.buzzsumo.com/search/articles.json"

    keyword = 'artificial intelligence'

    querystring = {"q":keyword,"domains":domain,"num_results":"100","num_days":"365","api_key":"BcsUWTlosJwlMJNT30h1pUXy05tugM1h"}

    response = requests.request("GET", url, params=querystring)

    responsejson = json.loads(response.text)
    #print(responsejson)


    df = pd.DataFrame(responsejson['results'])
    return df
    
print(getarticleshares('nytimes.com'))





finaldf = pd.DataFrame()
finaldf2 = pd.DataFrame()

for listitem in thelist:
    try:
        sitedf = getarticleshares(listitem)
        finaldf = finaldf.append(sitedf)
        finaldf2 = finaldf2.append(finaldf)
    except:
        pass
    
print(finaldf2)
finaldf.to_csv('finalshare3.csv')
