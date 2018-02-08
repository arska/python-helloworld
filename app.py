from flask import Flask
import os
import pymysql
app = Flask(__name__)

@app.route("/")
def hello():
    result = "<p><b>Hello World!</b></p><p>This is {host}</p><p>The message is {message}</p>".format(host=os.environ.get('HOSTNAME','localhost'), message=os.environ.get('MESSAGE','none'))

    mysqlconn = pymysql.connect(host=os.environ.get('AMAZEEIO_DB_HOST'), port=int(os.environ.get('AMAZEEIO_DB_PORT')), user=os.environ.get('AMAZEEIO_DB_USERNAME'), passwd=os.environ.get('AMAZEEIO_DB_PASSWORD'), db=os.environ.get('AMAZEEIO_SITENAME'))
    mysqlcursor = mysqlconn.cursor()
    mysqlcursor.execute('SELECT 1;')
    for row in mysqlcursor:
        result += "<p>MySQL: {0}".format(row)

    for env in os.environ:
        result += "<p>{0}={1}</p>".format(env,os.environ.get(env))
    return result

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=3000)
