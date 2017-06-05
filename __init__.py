import checknet
import status
import socket
import subprocess
import time
from  firebase import db
import os.path
import asyncio
import websockets
import json
scriptpath = os.path.dirname(__file__)
filename = os.path.join(scriptpath, 'config')
with open (filename,"r") as file:
	uid=file.read()
while True :
	if checknet.is_connected():
		print("==========Online===========")
		tempStatus=status.getStatus()
		myMac=list(tempStatus.keys())[0]
		print(myMac)
		try:
			command=db.child("users").child(uid).child("status").child(myMac).child("command").get().val()
			shutdown=db.child("users").child(uid).child("status").child(myMac).child("shutdown").get().val()
			print(command," ",shutdown)
			if command is not None and command!="-":
				subprocess.getoutput(command)
				#print(subprocess.getoutput(command))
				result=subprocess.getoutput(command)
				db.child("users").child(uid).child("status").child(myMac).child("result_command").set(result)
				print("command : ", command)
			if shutdown is not None and shutdown==1:
				#db.child("users").child(uid).child("status").child(myMac).child("shutdown").set(0)
				subprocess.getoutput('sudo shutdown -h now')
				print("shutdowned")
			db.child("users").child(uid).child("status").update(tempStatus)
			print("Send status to Firebase finished")
		except :
			print("Not found uid")
	else:
		print("==========Offline=========")
		@asyncio.coroutine
		def transfer(websocket, path):
        		yield from websocket.send(json.dumps(status.getStatus()))
        		datarecv = yield from websocket.recv()
        		print("< {}".format(datarecv))
		my_ip=socket.gethostbyname(socket.gethostname())
		start_server = websockets.serve(transfer,my_ip, 33333)
		asyncio.get_event_loop().run_until_complete(start_server)
		asyncio.get_event_loop().run_forever()
