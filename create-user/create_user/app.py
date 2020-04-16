from tools import mysql
import json

hostname = 'databasetest.cwuhw4ptyj4d.eu-west-3.rds.amazonaws.com'
username = 'TestAdmin'
password = '110193Do'
database = 'TestUser'

def lambda_handler(event, context):

    # res = []
    query = "INSERT INTO User(nom, prenom, age) VALUES(%nom,%prenom,%age)"
    args = {"nom":event['nom'], "prenom":event['prenom'], "age":event['age']}

    print(event)
    db = mysql.create_connection(hostname, username, password, database)
    cur = db.cursor()
    try:
        res = cur.execute(query, args)
        print(res)

    except ValueError:
        print(ValueError)

    finally:
        cur.close()
        db.close()

    # return {
    #     "statusCode": 201,
    #     "body": json.dumps(res)
    # }