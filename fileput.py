#!/usr/bin/env python

#
# fileput.py		Simple file put to S3
# author		Brian Walter @briantwalter
# version		0.0.1
# description		Use the Boto SDK and S3 API to put
#			and upload contents to S3 storage
#

# imports
import sys
from  ConfigParser import SafeConfigParser
from boto.s3.connection import S3Connection
from boto.s3.key import Key

# read configs
config = SafeConfigParser()
config.read('config.py')
acckey = config.get('fileput', 'acckey')
seckey = config.get('fileput', 'seckey')
bucket = config.get('fileput', 'bucket')

# get file name from command line
filename = str(sys.argv[1])
print "INFO: the local filename is " + filename

# make HTTPs connection to S3
conn = S3Connection(acckey, seckey)

# set the bucket name we're using
buck = conn.get_bucket(bucket)

# create a new key in S3 to store data in
key = Key(buck)

# set the name of the key (file) we're going to use
key.key = "index.html"

# write the contents from a local file to S3 key (file)
key.set_contents_from_filename(filename)
print "INFO: wrote contents from " + filename + " to " + str(key.key)
