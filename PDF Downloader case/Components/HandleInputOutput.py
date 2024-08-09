from Components.CheckIfExit import CheckIfExit
from Components.HandleMenuOptions import HandleMenuOptions

def HandleInputOutput():
    # This boolean keeps the loop running until it's time to exit the program
    loopShouldBeRunning = True
    
    # The following line prints the welcome and choose language message
    HandleMenuOptions("START")
    askingForLanguage = input()
    
    # CheckIfExit returns False unless you enter one of the exit strings ("EXIT", "LUK", "QUIT", "Q", "L", "STOP", "X")
    loopShouldBeRunning = CheckIfExit(askingForLanguage) == False
    
    # This loop runs until you enter one of the exit strings
    while loopShouldBeRunning:         
        # Gets the recurring menu with your options
        HandleMenuOptions(askingForLanguage) 
         
        # Asks for input from the user
        loopInputVariable = input()
        
        # Making sure the new input is not an exit string
        loopShouldBeRunning = CheckIfExit(loopInputVariable) == False 
        
        # Shows the result of the chosen input, then back to the start of the loop
        HandleMenuOptions(loopInputVariable) 
        