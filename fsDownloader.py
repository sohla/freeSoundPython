#!/usr/bin/env python
# encoding: utf-8
"""
untitled.py

Created by soh_la on 2012-08-01.
Copyright (c) 2012 soh_la. All rights reserved.
"""

import sys
import os
from subprocess import call

import errno

import getopt
from freesound import freesound
import urllib2


help_message = '''
fsDownloader

[options]
	-- help 		
	-- duration (int)
		max length in seconds
	-- license (int) 	
		# 0 - Creative Commons 0
		# 1 - Attribution
		# 2 - Attribution Noncommercial

[args]
	search terms
'''

freesound_client = freesound.FreesoundClient()
freesound_client.set_token("bfa791a021762f7c6cb70088c720855a0c5f8f49")


class Usage(Exception):
	def __init__(self, msg):
		self.msg = msg

	

def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc: # Python >2.5
        if exc.errno == errno.EEXIST:
            pass
        else: raise	


def pullSound(d,sound):

	# pull sound from freesound 
	withkey = '?api_key='+api_keys.freesound_api_key

	soundurl = sound['serve']
	u = urllib2.urlopen(soundurl + withkey)

	# need to read/write in chunks
	CHUNK = 16 * 1024
	snd_path = d + '/' + sound['original_filename']
	with open(snd_path,'w') as localFile:
		while True:
			chunk = u.read(CHUNK)
			if not chunk: break
			localFile.write(chunk)
		localFile.close()

		#all good, lets do something...			
		# playSound(snd_path)			
	
	return snd_path

def init():
	return 


def main(argv=None):
	if argv is None:
		argv = sys.argv
	try:
		try:
			opts, args = getopt.getopt(argv[1:], "hdlam:v:", ["help","duration=","license=","amount=","mp3="])
		except getopt.error, msg:
			raise Usage(msg)

		# init options
		s_min_duration = str(0)
		s_max_duration = str(60)
		s_license_code = 0;
		s_amount = str(150);
		s_license = " license:\"Creative Commons 0\""
		s_download = True

		# option processing
		for option, value in opts:
			if option == "-v":
				verbose = True
			if option in ("-h", "--help"):
				raise Usage(help_message)
			if option in ("-d", "--duration"):
				s_max_duration = str(value)
			if option in ("-l", "--license"):
				s_license_code = str(value)
			if option in ("-a", "--amount"):
				s_amount = str(value)
			if option in ("-m", "--mp3"):
				s_download = value
				
		# license codes :
		# 0 - Creative Commons 0
		# 1 - Attribution
		# 2 - Attribution Noncommercial

		
		if(s_license_code == "0"):
			s_license = " license:\"Creative Commons 0\""
		elif(s_license_code == "1"):
			s_license = " license:\"Attribution\""
		elif(s_license_code == "2"):
			s_license = " license:\"Attribution Noncommercial\""
			
		# init args
		s_query = ""
		for a in args:
			s_query = s_query + a + " +"

		s_query = s_query.strip(" +")

		# build params and search
		s_duration = " duration:["+  s_min_duration +" TO "+ s_max_duration+"]"
		s_filter = s_duration + s_license
		print "searching for %s %s" % (s_query,s_filter)
		result = freesound_client.text_search(query=s_query,page_size=s_amount, filter=s_filter,sort="rating_desc",fields="id,name,tags,username,license,previews")

		total = result.count

		if total > int(s_amount):
			total = int(s_amount)
		print "found %s sounds" % (total) 


		if s_download == True:
			# put samples in new dir
			s_query = s_query.replace(" +","&")
			new_dir = s_query + "_sounds"
			mkdir_p(new_dir)

			for sound in result:
				print "downloading....\t-", sound.name, "id:", sound.id
				file_name = sound.name+"_"+str(sound.id)+"_hq.mp3"
				sound.retrieve_preview(directory=new_dir,name=file_name)
		

			
	except Usage, err:
		print >> sys.stderr, sys.argv[0].split("/")[-1] + ": " + str(err.msg)
		print >> sys.stderr, "\t for help use --help"
		return 2


if __name__ == "__main__":
	init()
	sys.exit(main())
