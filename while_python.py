password = "random"
correct = False

while not correct:
    answer = input("What is the password? ")
    
    if answer == password:
        print("Access Granted")
        print("Welcome to the system")
        correct = True
    else:
        print("Access Denied")
        print("Try again...")