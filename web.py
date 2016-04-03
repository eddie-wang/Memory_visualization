from pymongo import MongoClient
from flask import Flask , request,render_template
import json
client = MongoClient('localhost',27017)
db=client.memory
app= Flask(__name__)
temp_time=0
@app.route('/')
def index():
	global temp_time
	temp_time=0
	return render_template('index.html')
@app.route('/data')
def data():
	global temp_time
	cursor=db.memory.find({"time":{"$gt":temp_time/1000}})
	arr=[]
	for data in cursor:
		arr.append([data["time"]*1000,data["mem"]])
	if len(arr)>0:
		temp_time=arr[-1][0]
	return json.dumps(arr)
if __name__=='__main__':
	app.run(host='0.0.0.0',port=9092,debug=True)