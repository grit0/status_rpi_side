import checknet

with open ("config","r") as file:
        uid=file.read()

while True :
	if checknet.is_connected() and uid is not '' :
		print("==========Online===========")
	else:
		print("offline")
