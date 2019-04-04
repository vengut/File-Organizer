import os
import shutil
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import operator
from collections import Counter
import fnmatch
import datetime

matchvalue = {}
logfile = open("logfile.txt","a")
logfile.write("%s\n" % (datetime.datetime.now()))
for file in os.listdir(os.curdir):
	if fnmatch.fnmatch(file, '*.mkv') and (os.path.getsize(file) >> 20) < 400:
		#print file
		matchvalue = {}
		for root,dirs,files in os.walk(os.curdir):
			for name in dirs:
				matchvalue[os.path.join(root,name)] = fuzz.partial_ratio(name,file)
		src = os.path.join(os.curdir,file)
		des = os.path.join(max(matchvalue.iteritems(), key=operator.itemgetter(1))[0],file)
		logfile.write("src: %s\ndes: %s\n" % (src,des))
		shutil.move(src,des)
logfile.close()