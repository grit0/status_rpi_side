import checknet
import status
import socket
import subprocess
import time
from threading import Thread
from  firebase import db
import os.path
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
scriptpath = os.path.dirname(__file__)
filename = os.path.join(scriptpath, 'config')
with open (filename,"r") as file:
	uid=file.read()
while True :
	if checknet.is_connected() and uid is not '' :
		print("==========Online===========")
		try:
	                db.child("users").child(uid).child("status").update(status.getStatus())
		except :
			print("Not found uid")
	else:
		print("==========Offline===========")
#		server = socket.socket()         
		#HOSTNAME = subprocess.getoutput("hostname -I | cut -d' ' -f1")
#		HOSTNAME = socket.gethostbyname(socket.gethostname())
#		PORT = 55555               
#		server.bind((HOSTNAME,PORT))      
#		server.listen(5)
#		print("Wait connect.....")
#		client,addr = server.accept()    
#		print('Connection from', addr)   
		#data=status.getStatus()
#		data="Helooooooooooooooooooooo"
#		while True:
#			client.send(data.encode('utf-8'))
#		client.close()   

