from flask import Flask
import os
import pymysql
import psycopg2

app = Flask(__name__)

@app.route("/")
def hello():
    result = "<p><b>Hello World!</b></p><p>This is {host}</p><p>The message is {message}</p>".format(host=os.environ.get('HOSTNAME','localhost'), message=os.environ.get('MESSAGE','none'))

    try:
        mysqlconn = pymysql.connect(host=os.environ.get('AMAZEEIO_DB_HOST'), port=int(os.environ.get('AMAZEEIO_DB_PORT')), user=os.environ.get('AMAZEEIO_DB_USERNAME'), passwd=os.environ.get('AMAZEEIO_DB_PASSWORD'), db=os.environ.get('AMAZEEIO_SITENAME'))
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

    for env in os.environ:
        result += "<p>{0}={1}</p>".format(env,os.environ.get(env))
    return result

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=3000)
