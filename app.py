from flask import Flask
import os
import pymysql
import psycopg2
import redis

app = Flask(__name__)

@app.route("/")
def hello():
    result = "<p><b>Hello World!</b></p><p>This is {host}</p><p>The message is {message}</p>".format(host=os.environ.get('HOSTNAME','localhost'), message=os.environ.get('MESSAGE','none'))

    try:
        mariadbhost = 'mariadb'
        mariadbport = 3306
        mariadbuser = os.environ.get('MARIADB_USERNAME') if os.environ.get('MARIADB_USERNAME') else 'lagoon'
        mariadbpasswd = os.environ.get('MARIADB_PASSWORD') if os.environ.get('MARIADB_PASSWORD') else 'lagoon'
        mariadbdb = os.environ.get('MARIADB_DATABASE') if os.environ.get('MARIADB_DATABASE') else 'lagoon'
        mysqlconn = pymysql.connect(host=mariadbhost, port=int(mariadbport), user=mariadbuser, passwd=mariadbpasswd, db=mariadbdb)
        mysqlcursor = mysqlconn.cursor()
        mysqlcursor.execute('SELECT 1;')
        for row in mysqlcursor:
            result += "<p>MySQL: {0}".format(row[0])
    except Exception as e:
        result += "<p>MySQL failed: {0}</p>".format(e)

    try:
        postgreshost = 'postgres'
        postgresport = 5432
        postgresuser = os.environ.get('POSTGRES_USERNAME') if os.environ.get('POSTGRES_USERNAME') else 'lagoon'
        postgrespassword = os.environ.get('POSTGRES_PASSWORD') if os.environ.get('POSTGRES_PASSWORD') else 'lagoon'
        postgresdbname = os.environ.get('POSTGRES_DATABASE') if os.environ.get('POSTGRES_DATABASE') else 'lagoon'
        pgsqlconn = psycopg2.connect(host=postgreshost, port=postgresport, user=postgresuser, password=postgrespassword, dbname=postgresdbname)
        pgsqlcursor = pgsqlconn.cursor()
        pgsqlcursor.execute('SELECT 1;')
        for row in pgsqlcursor:
            result += "<p>PostgreSQL: {0}".format(row[0])
    except Exception as e:
        result += "<p>PostgreSQL failed: {0}</p>".format(e)

    try:
        redishost = 'redis'
        redisport = 6379
        redispassword = os.environ.get('REDIS_PASSWORD', None)
        redisconn = redis.StrictRedis(host=redishost, port=redisport, password=redispassword)
        result += "<p>Redis: {0}</p>".format(redisconn.ping())
    except Exception as e:
        result += "<p>Redis failed: {0}</p>".format(e)


    for env in os.environ:
        result += "<p>{0}={1}</p>".format(env,os.environ.get(env))
    return result

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080)
