from tools import mysql
import json

hostname = 'databasetest.cwuhw4ptyj4d.eu-west-3.rds.amazonaws.com'
username = 'TestAdmin'
password = '110193Do'
database = 'TestUser'

def lambda_handler(event, context):

    res = []

    print(event)
    print(context)
    db = mysql.create_connection(hostname, username, password, database)

    cur = db.cursor()
    cur.execute("SELECT * FROM User")

    for row in cur.fetchall():
        res.append({'ID':row[0], 'Firstname':row[1], 'Name':row[2], 'Age':row[3]})

    db.close()
    return {
        "statusCode": 200,
        "body": json.dumps(res)
    }