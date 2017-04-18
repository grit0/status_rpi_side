import checknet
import status
import socket
import subprocess
import time
from threading import Thread
from  firebase import db
#from multiprocessing import Process
#print(status.getStatus())
#if __name__=='__main__':
#	a1=Process(firebase.sendToFirebase(status.getStatus()))
#	a2=Process(firebase.sendToFirebase(status.getStatus()))
#	a1.start()
#	a2.start()
#	a1.join()
#	a2.join()
	#print("send Finish")
#while(True):
	#firebase.sendToFirebase(status.getStatus())
with open ("config","r") as file:
	uid=file.read()
if checknet.is_connected() and uid is not '' :
	print("==========Online===========")
	#db.child("users").child(uid).child("status").update(status.getStatus())
	#firebase.sendToFirebase(status.getStatus())
	try:

            while(checknet.is_connected()):
                    db.child("users").child(uid).child("status").update(status.getStatus())
		#print("Debug")
		#time.sleep(5)
		#print("Debug2")
		#status.runCommand()
		#db.child("users").child(uid).child("status").update(status.getStatus())
	except :
		print("Not found uid")
else:
	print("==========Offline===========")
	server = socket.socket()         
	#HOSTNAME = subprocess.getoutput("hostname -I | cut -d' ' -f1")
	HOSTNAME = socket.gethostbyname(socket.gethostname())
	PORT = 55555               
	server.bind((HOSTNAME,PORT))      
	server.listen(5)
	print("Wait connect.....")
	client,addr = server.accept()    
	print('Connection from', addr)   
	#data=status.getStatus()
	data="Helooooooooooooooooooooo"
	while True:
		client.send(data.encode('utf-8'))
	client.close()   

