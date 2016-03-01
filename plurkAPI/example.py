from plurk_oauth import plurkAPI

#Replace the following keys and secrets with your app's.
#You can retrieve your app keys via the test tool at http://www.plurk.com/PlurkApp/
app_key = 'CONSUMER_KEY'
app_secret = 'CONSUMER_SECRET'
token= 'ACCESS_TOKEN'
token_secret='ACCESS_TOKEN_SECRET'

plurk=plurkAPI(app_key,app_secret,token,token_secret)


data=plurk.callAPI('/APP/Timeline/getUnreadPlurks',{'offset':'2014-1-20T21:55:34'})
print(data)

content=('The plurk is posted via plurkAPI.')
qualifier=('says')
plurk.callAPI('/APP/Timeline/plurkAdd',{},{'content':content,'qualifier':qualifier})