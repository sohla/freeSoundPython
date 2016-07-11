import os
import sys
from freesound import freesound

from requests_oauthlib import OAuth2Session
from oauthlib.oauth2 import BackendApplicationClient

os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'


client_id = 'f2880da706c6d92d7ce3'
client_secret = 'bfa791a021762f7c6cb70088c720855a0c5f8f49'

auth_url = 'https://www.freesound.org/apiv2/oauth2/authorize/'
token_url = 'https://www.freesound.org/apiv2/oauth2/access_token/'
redirect_uri = 'https://www.freesound.org/home/app_permissions/permission_granted/'




oauth = OAuth2Session(client_id, redirect_uri=redirect_uri)

# authorization_url, state = oauth.authorization_url(auth_url)
# print 'Please go to \n -> \t %s \t <-  \n and authorize access.' % authorization_url

## copy from browser ##
# authorization_response = "https://www.freesound.org/home/app_permissions/permission_granted/?state=FcsyRqhWdCUuGuSPcHicXsv4weKrMt&code=40s57OeSbP4yD2ipUpomlGcZXSWKRE"
# token = oauth.fetch_token(token_url, authorization_response=authorization_response)
# print token.access_token


## TODO : work in the refresh_token


freesound_client = freesound.FreesoundClient()
freesound_client.set_token("ymgL9XPzSyjLHj1kWSufNnzqFife6S", auth_type='oauth')

# Get sound info example
print "Sound info:"
print "-----------"
sound = freesound_client.get_sound(96541)
print "Getting sound:", sound.name
print "Url:", sound.url
print "Description:", sound.description
print "Tags:", " ".join(sound.tags)
print

sound.retrieve("")

