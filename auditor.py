inventory = 0
invEntry = 0

def Report():
    print("Printing Report....")
    print("Total Units Processed: ", inventory)
    print("Number of Failed/Rejected Entries: ", invEntry)
    return


while 1:
    userInput = input("Please Enter stock quantity: ")

    if userInput.lower() == "quit":
        Report()
        print("Exiting Program....")
        break

    if not userInput.isdigit():
        print("Invalid number, please try again!")
        invEntry += 1
        continue

    if inventory + int(userInput) > 500:
        Report()
        print("Overstock detected! Teminating Program...")
        break
    
    inventory += int(userInput)
    print("Inventory Updated! Current inventory: ", inventory)

    