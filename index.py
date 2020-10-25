#!C:\Program Files\Python37\python.exe
print("Content-type:text/html\n\n")
# import win_unicode_console
# win_unicode_console.enable()


import views

html= views.head() + views.index() + views.footer()
#html=views.home()
#html= views.sody()
# ttml= views.head()
# ztml=views.home
print(html)
# print(ttml)
# print(ztml)