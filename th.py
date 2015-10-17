import subprocess
import os
import time
import datetime
from PIL import Image
import threading
import Queue
import re
#import psycopg2
import uuid

lsdir = "/root/v4/"
rootdir = '/root/dummy/th/'
logfile =  "/root/dummy/read.txt"
sqlfile =  "/root/dummy/sql.txt"
lsdirs = os.listdir(lsdir)

f = open(logfile, 'a')
s = open(sqlfile, 'a')
THdir = []


for vs in lsdirs:	
	#videofile = lsdir + vs
	filename = lsdir + vs
	extension = os.path.splitext(filename)[1]
	curtime  = uuid.uuid4().hex
	new_file_name = lsdir + 'VD_%s%s' % (curtime, extension)
	os.rename(filename, new_file_name)
