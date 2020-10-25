#!C:\Program Files\Python37\python.exe
print("Content-type: text/html\n\n")
# import win_unicode_console
# win_unicode_console.enable()


import views
import cgi, cgitb; cgitb.enable()

form=cgi.FieldStorage()
tweet_id=form['id'].value

html= views.head() + views.reply(tweet_id) + views.footer()

print(html)  