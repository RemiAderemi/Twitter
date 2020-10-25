 
print('remi is ere')

import mysql.connector

def db_connect():
    db=mysql.connector.connect(host='Localhost',User='root',passwd='',database='twitter')
    if(db):
        return db
    else:
        print("connection Unsucessful")
print(db_connect)