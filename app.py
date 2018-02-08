from flask import Flask
import os
app = Flask(__name__)

@app.route("/")
def hello():
    result = "<p><b>Hello World!</b></p><p>This is {host}</p><p>The message is {message}</p>".format(host=os.environ.get('HOSTNAME','localhost'), message=os.environ.get('MESSAGE','none'))
    for env in os.environ:
        result += "<p>{0}={1}</p>".format(env,os.environ.get(env))
    return result

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=3000)
