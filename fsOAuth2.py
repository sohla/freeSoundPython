import os
import sys
from freesound import freesound
import json
from argparse import Namespace

from requests_oauthlib import OAuth2Session
from oauthlib.oauth2 import BackendApplicationClient

def byteify(input):
    if isinstance(input, dict):
        return {byteify(key): byteify(value)
                for key, value in input.iteritems()}
    elif isinstance(input, list):
        return [byteify(element) for element in input]
    elif isinstance(input, unicode):
        return input.encode('utf-8')
    else:
        return input

os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'


client_id = 'f2880da706c6d92d7ce3'
client_secret = 'bfa791a021762f7c6cb70088c720855a0c5f8f49'

auth_url = 'https://www.freesound.org/apiv2/oauth2/authorize/'
token_url = 'https://www.freesound.org/apiv2/oauth2/access_token/'
redirect_uri = 'https://www.freesound.org/home/app_permissions/permission_granted/'




oauth = OAuth2Session(client_id, redirect_uri=redirect_uri)

# # request authorization
# authorization_url, state = oauth.authorization_url(auth_url)
# print 'Please go to \n -> \t %s \t <-  \n and authorize access.' % authorization_url

## copy from browser ##

# authorization_response = redirect_uri + "?state=0zCOKkgbr4GaKcg5oxhnmaOpYlRL4L&code=bIbZS34egvf7Vpfu9hKEdoy59AaPhp"
authorization_response = "https://www.freesound.org/home/app_permissions/permission_granted/?state=DL8yQ8HHGKFFD9s7wN2sxanf9h0Vxq&code=tnuH4jDsZxBBRE1ZNQIjMtUKMfeOA6"
token = oauth.fetch_token(token_url, authorization_response=authorization_response)

## test token
# token = {u'token_type': u'Bearer', u'refresh_token': u'LhGsmAax4VQ7DHxI2SgOIz9DDaWouY', u'access_token': u'hLUULRU1UnqaopEgHP1MayLWocoVWb', u'scope': [u'read', u'write'], u'expires_in': 36000, u'expires_at': 1468281745.159104};

# extract token from json
access_token = byteify(token).get("access_token")
refresh_token = byteify(token).get("refresh_token")
print "refresh -> ", refresh_token
print "access -> ", access_token


## TODO : work in the refresh_token


# freesound_client = freesound.FreesoundClient()
# freesound_client.set_token("ymgL9XPzSyjLHj1kWSufNnzqFife6S", auth_type='oauth')

# # Get sound info example
# print "Sound info:"
# print "-----------"
# sound = freesound_client.get_sound(96541)
# print "Getting sound:", sound.name
# print "Url:", sound.url
# print "Description:", sound.description
# print "Tags:", " ".join(sound.tags)
# print

# sound.retrieve("")

