inventory = 0

while 1:
    userInput = input("Please Enter stock quantity: ")

    if userInput.lower() == "quit":
        break
    
    inventory += int(userInput)
    print("Inventory Updated! Current inventory: ", inventory)