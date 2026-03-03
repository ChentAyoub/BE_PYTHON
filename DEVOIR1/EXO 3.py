mdp= "python123"
while True:
    password = input("Enter the password: ")
    if password == mdp:
        print("password correct")
        break
    else:
        print("password incorrect try again")