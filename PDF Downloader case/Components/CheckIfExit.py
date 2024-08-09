def CheckIfExit(inputMessage):    
    # A list of all the inputs that will exit the program
    exitArray = ["EXIT", "LUK", "QUIT", "Q", "L", "STOP", "X"]
    # In case it's a number, turn it to a string
    input = str(inputMessage)
    
    # If the input is capitalized
    if input.isupper():
        # Save it as is
        inputUppercase = input
    else: # Else capitalize it
        inputUppercase = input.upper()
    
    # Looping through the exit strings
    for i in exitArray:
        # If the input matches a exit string
        if inputUppercase == i:
            # Stop the program
            exit()
            
    # If the input does not match any of them return false
    return False