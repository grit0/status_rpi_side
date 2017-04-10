import checknet
import status
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
	#firebase.sendToFirebase(status.getStatus())
	try:
		db.child("users").child(uid).child("status").update(status.getStatus())
	except :
		print("Not found uid")
else:
	print("==========Offline===========")


