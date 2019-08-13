#!/usr/bin/python

from twitter import *
import sys
import csv
import time
import os

try:	
	latitude = float(29.76)
	longitude = float(-95.36)
	max_range = float(52) #unit: km
	num_results = 100 # pull 100 tweets per precess

	outfile = "output" + str(time.time()) + ".csv"
	
	config = {}
	execfile("config.txt", config) # convert to 3.0
	
	# create twitter API object
	twitter = Twitter(auth=OAuth(config["access_key"], config["access_secret"],\
                              config["consumer_key"], config["consumer_secret"]))
	
	# open a file to write (mode "w"), and create a CSV writer object
	csvfile = file(outfile, 'w') # convert to 3.0
	csvwriter = csv.writer(csvfile)
	
	# add headings to our CSV file
	row = ["Username", "Profile URL", "Latitude", "Longitude","Google Maps","Tweet", "Time"]
	csvwriter.writerow(row)
	result_count = 0
	last_id = None
	while result_count < num_results:
		
		# perform a search based on latitude and longitude
		query = twitter.search.tweets(q="", geocode="%f,%f,%dkm" % (latitude, longitude, max_range)\
                                , num_results=100, max_id=last_id)
        # q: keyword
		for result in query["statuses"]:
			
			# only process a result if it has a geolocation
			if result["geo"]:
				user = result["user"]["screen_name"]
				text = result["text"]
				text = text.encode('ascii', 'replace')
				latitude = result["geo"]["coordinates"][0]
				longitude = result["geo"]["coordinates"][1]
				timet = result["created_at"]
				url = 'https://twitter.com/%s' % user
				gurl = 'https://maps.google.com/?q=' + str(latitude) + ',' + str(longitude)
				
				# now write this row to our CSV file
				row = [user, url, latitude, longitude,gurl, text, timet]
				csvwriter.writerow(row)
				result_count += 1
				time.sleep(.35)
			last_id = result["id"]
			
	# let the user know where we're up to
	
	if result_count == 1:
		csvfile.close()
	elif result_count == 0:

	else:
		csvfile.close()
	
	# we're all finished, clean up and go home.
	
	
except ImportError:
	print 'error message'
    
print 'computation is finished'