from  firebase import db
import subprocess
import RPi.GPIO as GPIO   
uid="11QyDZZsHTUmh0gKoBzW8OZjPB73"
myMac='b8:27:eb:49:e3:4a'
#db_current=db.child("users").child(uid).child("status").child(myMac)
#try:
#command=db.child("users").child(uid).child("status").child(myMac).child("command").get().val()
#shutdown=db.child("users").child(uid).child("status").child(myMac).child("shutdown").get().val()
#if command is not None and command=="-":
#	print("command : ", command)
#	subprocess.getoutput(command)
#	db.child("users").child(uid).child("status").child(myMac).child("command").set("-")
#if shutdown is not None and shutdown==1:
#	db.child("users").child(uid).child("status").child(myMac).child("shutdown").set(0)
	#subprocess.getoutput('sudo shutdown -h now')
#	print("shutdowned")
#for i in range(1,41):
#	pin=db.child("users").child(uid).child("status").child(myMac).child("peripheral/gpio").child(i).get().val()	
#	print(i,"--> mode: ",pin['mode'],"   value: ",pin['value'])
#	if pin['mode'] in 
GPIO.setmode(GPIO.BOARD)

#pin=db.child("users").child(uid).child("status").child(myMac).child("peripheral/gpio").child(24).get().val()
gpio_firebase=db.child("users").child(uid).child("status").child(myMac).child("peripheral/gpio").child(24)
#print(pi.child("value").get().val())
print(gpio_firebase.get().val())
#print("pin : ",db.child("users").child(uid).child("status").child(myMac).child("peripheral/gpio").child(24).child("name").get().val())
#print("va : ",db.child("users").child(uid).child("status").child(myMac).child("peripheral/gpio").child(24).child("value").get().val())
print("start try")
try:
	for i in range(1,41) :
		print(i,db.child("users").child(uid).child("status").child(myMac).child("peripheral/gpio").child(i).child("modeIN").get().val())
		print(not db.child("users").child(uid).child("status").child(myMac).child("peripheral/gpio").child(i).child("modeIN").get().val())
		if not db.child("users").child(uid).child("status").child(myMac).child("peripheral/gpio").child(i).child("modeIN").get().val():			
			try:
				GPIO.setup(i,GPIO.OUT)
				GPIO.output(i,db.child("users").child(uid).child("status").child(myMac).child("peripheral/gpio").child(i).child("value").get().val())
			except ValueError:
				print("valueerror")
		#GPIO.output(24,True)
		#	GPIO.setwarnings(False) 
			#GPIO.output(24,db.child("users").child(uid).child("status").child(myMac).child("peripheral/gpio").child(i).child("value").get().val()) 		
#	if pin['mode'] == "IN":
#		print("in")
#		GPIO.setup(24, GPIO.IN)
#	if pin['mode'] == "OUT":
#        	GPIO.setup(24, GPIO.OUT)
except:
	print("error")

#if pin['value'] == "1":
#        GPIO.output(24, GPIO.HIGH)
#if pin['value'] == "0":
#        GPIO.output(24, GPIO.LOW)
#except:
#	print("Not haven't status control")
#print(subprocess.getoutput(command))
#subprocess.getoutput(command)
