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
tweet_name = form.getvalue("tweet_name")
tweet_text  = form.getvalue("tweet_text")
reply_name=form.getvalue("reply_name")
reply_text=form.getvalue("reply_text")
parent_tweet_id=form.getvalue("tweetid")
#imagepath=form['image_path']
dateTime = datetime.utcnow().strftime('%Y-%m-%d %H:%H:%S')

#image_path=form.getvalue("tweetimage") cannot use getvalue for images

# fileitem=form["filename"]
# if fileitem.filename:
#     fn=os.path.basename(fileitem.filename)
#     open(fn,'wb').write(fileitem.file.read())
#     print("the file was uploaded sucessfully")
# else:
#     print("the upload was unsuccesful")

fileitem=form['image_path']
if fileitem.filename:# mean cheking if the filaname exist oor not
    # strip leading path from file name to avoid
    # directory traversal attacks
    fn = os.path.basename(fileitem.filename)
    fn = fn.replace(" ", "_")
    open('userimages/' + fn, 'wb').write(fileitem.file.read())
    imageurl = BASE_URL+'userimages/'+fn
    usrmsg = 'The file ' + fn + ' was uploaded successfully'
#print(fileitem)
# if fileitem.filename:
#    print(fileitem)
# #if fileitem.filename:#filename is a key in the array fileitem
#    fn= os.path.basename(fileitem.filename)#this is the file name9
#    fn = fn.replace(" ", "_")
   
  
# # open read and write the file into the server 
#    open('userimages/'+fn, 'wb').write(fileitem.file.read())#images/fn -> images/image1.jpg 
#    imageurl = BASE_URL+'/userimages/'+fn # http://localhost/twitter//images/image1.jpg
#    usrmsg = 'The file "' + fn + '" was uploaded successfully'
else:
   imageurl = False
   usrmsg = 'No file was uploaded'
   print(usrmsg)
if imageurl == False:
   imagepath = ''
else:
   imagepath = imageurl
if parent_tweet_id :
      re_tweet={'parent_tweet_id': parent_tweet_id,'name' : reply_name ,'image' : imagepath , 'description' : reply_text  , 'created_at' : dateTime}
      dataInsert=model.reply_tweet_data(re_tweet)        
else:
      tweet = {'title' : tweet_name , 'description' : tweet_text , 'image' : imagepath , 'created_at' : dateTime}
      dataInsert = model.post_tweet_data(tweet)





# the part below is the response segment from model.py
twitterResponse = json.loads(dataInsert)#json.dumps conver the jason.loads to readable for Serialization
if twitterResponse['status'] == 200:
   # print "Location:http://localhost/twitter-python/index.py"
   redirect = """<script>window.location.replace('http://localhost/zwitter/index.py')</script>"""
   print(redirect)
else:
   print("Data not insert") 

 #the part below is the response segment from model.py
# twitterResponse = json.loads(reply_tweet)#json.dumps conver the jason.loads to readable for Serialization
# if twitterResponse['status'] == 200:
#    # print "Location:http://localhost/twitter-python/index.py"
#    redirect = """<script>window.location.replace('http://localhost/zwitter/index.py')</script>"""
#    print(redirect)
# else:
#    print("Data not insert") 

