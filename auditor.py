inventory = 0

while 1:
    userInput = input("Please Enter stock quantity: ")

    if userInput.lower() == "quit":
        break

    if not userInput.isdigit():
        print("Invalid number, please try again!")
        continue
    
    inventory += int(userInput)
    print("Inventory Updated! Current inventory: ", inventory)