#countdown that accepts user input


import time

#Create countdown function
def set_countdown():
    #Ask for countdown input
    seconds = int(input("Enter amount of seconds: ")) #converts string to integer
    print("Countdown starts now...") 
    temp = seconds #keeps track of remaining time
    print(temp)
    while temp != 0: #While number does not equal 0, continue function
        if temp != seconds:
            print("\b"*len(str(temp))) #deletes previous number
        time.sleep(1) #1 second countdown delay for effect
        temp -= 1 #decrease number by 1
        print(temp, end="") #print current number
    print("\nCountdown ended...\n")

#Welcome user
print("==========Welcome to the countdown!==========")
while 1:
    choice = input("Would you like to set a countdown? (y/n): ") #Ask user if they want to set a countdown
    if "y" in choice.lower():
        set_countdown()
    elif "n" in choice.lower():
        print("Exiting countdown...")
        break
    else:
        print("Invalid input. Please select y or n")
