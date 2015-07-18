from flask import Flask,request,render_template
from flask.ext.cors import CORS
app = Flask(__name__)
cors = CORS(app)
import json

@app.route("/")
def hello():
    return render_template('hello.html',title="Hello");

@app.route("/convert", methods=["POST"])
def convert():
    data = request.form['data']
    print data
    fout = open('data.txt', 'w')
    fout.write(data)
    #fout.close()
    result = makeTree("data.txt")
    #print result.toJSON()
    return json.dumps(result.toJSON())

app.run()

