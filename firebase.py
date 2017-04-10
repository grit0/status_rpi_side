
import pyrebase
config = {                           
	"apiKey": "AIzaSyCMuM1Toy1upqRY1czF0YpkhxrAo2fzR4Q",
	"authDomain": "pi-grit.firebaseapp.com",
	"databaseURL": "https://pi-grit.firebaseio.com",
	"projectId": "pi-grit",
}                                                                                                                                                                                              
firebase = pyrebase.initialize_app(config)                                                                                                                                                     
auth = firebase.auth()
db = firebase.database() 
def sendToFirebase(data):
	db.update(data)
	#print(data)

