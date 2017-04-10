from firebase  import auth,db
import checknet
def log_in(email,password):
        try:
                user = auth.sign_in_with_email_and_password(email, password)
                print("log up finish")
                print(user)
        except :
                print("log in error")
        with open ("config","w") as file:
                file.write(user['localId'])
        return user['localId']
menu=["Log in","Offline","Singn up","Forget Password"]
if not checknet.is_connected():
        menu.pop()
        menu.pop()
for i in range(len(menu)):
        print(i+1,")",menu[i])
choice=input("Enter Choice : ")
if choice=="1" :#login
        while True:
                email=input("Email : ")
                password=input("Password : ")
                log_in(email,password)
                break
elif choice =="2" :#offline
        with open ("config","w") as file:
                file.write("")
        print("clear login")
else:
        if checknet.is_connected():
                if choice=="3" :#sign up
                        while True :
                                email=input("Email : ")
                                password=input("Password : ")
                                re_password=input("Re-Prassword : ")
                                if password == re_password :
                                        try:
                                                auth.create_user_with_email_and_password(email,password)
                                                print("sing up finish")
                                                uid=log_in(email,password)
                                                print("uid : ",uid)
                                                db.child("users").child(uid).set({"email":email,"password":password})
                                                break
                                        except :
                                                print("error")

                elif choice =="4" : #forget password
                        email=input("Email : ")
                        try:
                                auth.send_password_reset_email(email)
                        except :
                                print("INVALID_EMAIL")
