# -*- coding:utf-8 -*-
# coding:utf-8
import oauth2 as oauth
import urllib.parse
import json

class plurkAPI:
	def __init__(self,key=None,secret=None,token_key=None,token_secret=None):
		self.base_url = 'https://www.plurk.com'
		self.request_token_url = '/OAuth/request_token'
		self.authorization_url = '/OAuth/authorize'
		self.access_token_url = '/OAuth/access_token'
		self.sign_method = oauth.SignatureMethod_HMAC_SHA1()
		self.app_key=key
		self.app_secret=secret
		self.oauth_token=token_key
		self.oauth_token_secret=token_secret
		if key is None or secret is None:
			raise ValueError("APP_key and APP_secret is needed")

	def request(self,url,params=None):
		consumer=oauth.Consumer(self.app_key,self.app_secret)
		token=oauth.Token(self.oauth_token,self.oauth_token_secret)
		client=oauth.Client(consumer,token)
		request = oauth.Request.from_consumer_and_token(consumer=consumer, token=token, http_method='POST', http_url=url,parameters=params,is_form_encoded=True)
		request.sign_request(self.sign_method, consumer, token)
		return (request)
	
	def callAPI(self,url,params=None,data=None):
		req=self.request(self.base_url+url,params)
		consumer=oauth.Consumer(self.app_key,self.app_secret)
		token=oauth.Token(self.oauth_token,self.oauth_token_secret)
		client=oauth.Client(consumer,token)
		encoded_content = None
		if data:
			encoded_content = urllib.parse.urlencode(data)
		resp, content = client.request(self.base_url + url, "POST", headers=req.to_header(), body=encoded_content)
		if isinstance(content, bytes):
			content = content.decode('UTF-8')
		return resp['status'], content, resp.reason
			
	def get_request_token(self):
		consumer=oauth.Consumer(self.app_key,self.app_secret)
		client=oauth.Client(consumer)
		response=client.request(self.base_url+self.request_token_url,method='POST')
		response=dict(response)
		return (response)
		
	def get_access_token(self):
		consumer=oauth.Consumer(self.app_key,self.app_secret)
		token=oauth.Token(self.oauth_token,self.oauth_token_secret)
		token.set_verifier(self.oauth_verifier)
		client=oauth.Client(consumer,token)
		response=client.request(self.base_url+self.access_token_url,method='POST')
		return (response)
