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
        mariadbhost = os.environ.get('MARIADB_HOST') if os.environ.get('MARIADB_HOST') else 'mariadb'
        mariadbport = os.environ.get('MARIADB_PORT') if os.environ.get('MARIADB_PORT') else '3306'
        mariadbuser = os.environ.get('MARIADB_USERNAME') if os.environ.get('MARIADB_USERNAME') else 'lagoon'
        mariadbpasswd = os.environ.get('MARIADB_PASSWORD') if os.environ.get('MARIADB_PASSWORD') else 'lagoon'
        mariadbdb = os.environ.get('MARIADB_DATABASE') if os.environ.get('MARIADMARIADB_DATABASEB_PASSWORD') else 'lagoon'
        mysqlconn = pymysql.connect(host=mariadbhost, port=int(mariadbport), user=mariadbuser, passwd=mariadbpasswd, db=mariadbdb)
        mysqlcursor = mysqlconn.cursor()
        mysqlcursor.execute('SELECT 1;')
        for row in mysqlcursor:
            result += "<p>MySQL: {0}".format(row[0])
    except Exception as e:
        result += "<p>MySQL failed: {0}</p>".format(e)

    try:
        pgsqlconn = psycopg2.connect(host=os.environ.get('AMAZEEIO_POSTGRES_HOST'), port=int(os.environ.get('AMAZEEIO_POSTGRES_PORT')), user=os.environ.get('AMAZEEIO_POSTGRES_USERNAME'), password=os.environ.get('AMAZEEIO_POSTGRES_PASSWORD'), dbname=os.environ.get('AMAZEEIO_SITENAME'))
        pgsqlcursor = pgsqlconn.cursor()
        pgsqlcursor.execute('SELECT 1;')
        for row in pgsqlcursor:
            result += "<p>PostgreSQL: {0}".format(row[0])
    except Exception as e:
        result += "<p>PostgreSQL failed: {0}</p>".format(e)

    try:
        redishost = os.environ.get('REDIS_HOST') if os.environ.get('REDIS_HOST') else 'redis'
        redisport = os.environ.get('REDIS_PORT') if os.environ.get('REDIS_PORT') else '6379'
        redisconn = redis.StrictRedis(host=redishost, port=redisport)
        result += "<p>Redis: {0}</p>".format(redisconn.ping())
    except Exception as e:
        result += "<p>Redis failed: {0}</p>".format(e)


    for env in os.environ:
        result += "<p>{0}={1}</p>".format(env,os.environ.get(env))
    return result

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=3000)
