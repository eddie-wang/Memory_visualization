from subprocess import Popen , PIPE
import re,time
from pymongo import MongoClient
def getMem():
	vm=Popen("vm_stat",stdout=PIPE)
	result=vm.communicate()[0]
	free,total=0,0
	first=True
	for line in result.split('\n')[1:8]:
		total+=int(line[re.search("\d",line).start():-1])
		if first : free=total;first=False
	t=int(time.time())
	db.memory.insert_one({"mem":float(free)/total,"time":t})

client = MongoClient('localhost',27017)
db=client.memory
while True :
	time.sleep(1)
	getMem()