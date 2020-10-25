#!C:\Program Files\Python37\python.exe
print("Content-type:text/html\n\n")
# import win_unicode_console
# win_unicode_console.enable()
import sys
import os
import cgitb
from datetime import datetime
import json
import model
import cgi
cgitb.enable()

# Import modules for CGI handling
# import model
# import cgi, cgitb; cgitb.enable()
# import os, sys
# import json
# from datetime import datetime


# Create instance of FieldStorage

form = cgi.FieldStorage()
BASE_URL = os.environ.get("BASE_URL", "http://localhost/Zwitter/")
# Get data from fields

reply_name=form.getvalue("reply_name")
reply_text=form.getvalue("reply_text")
parent_tweet_id=form.getvalue("tweetid")
#imagepath=form['image_path']
dateTime = datetime.utcnow().strftime('%Y-%m-%d %H:%H:%S')


re_tweet={'parent_tweet_id': parent_tweet_id,'name' : reply_name , 'description' : reply_text  , 'created_at' : dateTime}

reply_tweet=model.reply_tweet_data(re_tweet)



#the part below is the response segment from model.py
twitterResponse = json.loads(reply_tweet)#json.dumps conver the jason.loads to readable for Serialization
if twitterResponse['status'] == 200:
   # print "Location:http://localhost/twitter-python/index.py"
   redirect = """<script>window.location.replace('http://localhost/zwitter/index.py')</script>"""
   print(redirect)
else:
   print("Data not insert")