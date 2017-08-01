from plurk_oauth import plurkAPI
import json
from pprint import pprint

#Replace the keys and secrets in oauth_key.json with your app's.
#You can retrieve your app keys via the test tool at http://www.plurk.com/PlurkApp/
raw_key_data = open('oauth_key.json').read()
key_data = json.loads(raw_key_data)
app_key = key_data.get('app_key')
app_secret = key_data.get('app_secret')
token = key_data.get('token')
token_secret = key_data.get('token_secret')

plurk=plurkAPI(app_key,app_secret,token,token_secret)

#Read all unread plurks and print to console
raw_data=plurk.callAPI('/APP/Timeline/getUnreadPlurks',{'offset':'2014-1-20T21:55:34'})
data=json.loads(raw_data[1])
pprint(data)

#Add new plurk
content=('The plurk is posted via plurkAPI.')
qualifier=('says')
plurk.callAPI('/APP/Timeline/plurkAdd',{},{'content':content,'qualifier':qualifier})
