from firebase  import auth,db
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
print("Login")
email=input("Email : ")
password=input("Password : ")
print(log_in(email,password))
