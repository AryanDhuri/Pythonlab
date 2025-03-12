registerd_email=[]



while True:
    email=input("enter ur email address: ")

    if email.lower() == 'quit':
        print("Exiting....")
        break

    if email in registerd_email:
        print("email already existing")
        

    else:
        registerd_email.append(email)
        print("email saved sucessfully")
        
