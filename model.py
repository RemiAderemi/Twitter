#!C:\Program Files\Python37\python.exe
import json
import mysql.connector


conn=mysql.connector.connect(host='localhost', user='root', passwd='',database='twitter')
conn.is_connected()


def create_table():
    sql= "create table users (id int auto_increment primary key, parent_tweet_id int, name varchar(50) not null, text varchar(250), created_at timestamp, image_path varchar(250));"
    
    cur=conn.cursor()
    cur.execute(sql)
    for x in cur:
        print(x)
        return x  

def get_tweet_data():
    sql= "select * from users"
    cur=conn.cursor()
    cur.execute(sql)
    view=cur.fetchall()
    return view

def post_tweet_data(value):
    sql= "insert into users (name,text,image_path, created_at) values('"+str(value['title'])+"','"+str(value['description'])+"','"+str(value['image'])+"', '"+str(value['created_at'])+"')"
    cur=conn.cursor()
    try:
        cur.execute(sql)
        conn.commit()
        dataResponse={'status':200, 'message':'data posted successfully'}
        conn.close()
        return json.dumps(dataResponse)
    except:
        conn.rollback()
        dataResponse={'status':400, 'message':'data  not posted successfully'}
        conn.close()
        return json.dumps(dataResponse)

def reply_tweet_data(value):
    sql= "insert into users (parent_tweet_id, name,text, image_path, created_at) values('"+str(value['parent_tweet_id'])+"','"+str(value['name'])+"','"+str(value['description'])+"','"+str(value['image'])+"', '"+str(value['created_at'])+"')"
    cur=conn.cursor()
    try:
        cur.execute(sql)
        conn.commit()
        reply_tweet={'status':200, 'message':'data posted successfully'}
        conn.close()
        return json.dumps(reply_tweet)
    except:
        conn.rollback()
        reply_tweet={'status':400, 'message':'data  not posted successfully'}
        conn.close()
        return json.dumps(reply_tweet)
    
def get_single_tweet(tweet_id):
    cur=conn.cursor()
    sql="Select * from users where id="+str(tweet_id)
    cur.execute(sql)
    result=cur.fetchone()
    return result

def reply_count(tweet_id):
    cur=conn.cursor()
    sql="Select count(*) from users where parent_tweet_id="+str(tweet_id)
    cur.execute(sql)
    result=cur.fetchone()
    return result
