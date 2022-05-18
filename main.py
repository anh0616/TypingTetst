from datetime import *
from function import *
import msvcrt


print("\n------------ TYPING TEST ------------")
print("-------------------------------------\n")

while True:
    print("Please choose the following options:")
    print("(1) Quick start")
    print("(2) Custom test")
    print("(3) Quit")

    menuInp = input("Your choice is: ") # Take in user input

    try:                                                
        int(menuInp)                                    # Convert input into an interger.
        if((int(menuInp) < 1) or (int(menuInp) > 3)):   # See if the input is in range.
            inpCheck = False
        else:
            if (int(menuInp) == 3):                     # Exit the program if the input is 3.
                exit()
            else:
                inpCheck = True
    except ValueError:                                  #'inpCheck = False' if the input is not int.
        inpCheck = False

    if (inpCheck == True):
        if not menuInp:             # 'inpCheck = False' if the input is empty.
            inpCheck = False

        if (int(menuInp) == 1):
            sample = "Hello World"  # Default sample text when the user input 1.
        elif(int(menuInp) == 2):
            sample = typeFileR()    # Import sample text from .txt when the user input 2.

        print("\n")
        print("Your text are:\n")
        print (sample)              # Show user the sample text.
        print("\n")

        print("-- Press any key to start or 'x' to quit --\n")
        pressedKey = msvcrt.getch() # Record user input in real time and put it in pressedKey.
        if (pressedKey[0] == 120):  # Quit the while loop when user input 'x' (120 is ascii code).
            inpCheck = False
        else:                       # If user input anything key, start the test. 
            print("GO...\n")
            sampleLen = wordCount(sample)                   # Take the lenght of the sample text.
            init_hrs, init_mins, init_secs = typeTimer()    # Take the time at the beginning.
            usrInput, usrResult, lostPoint = typeIn()       # Run the typing test.
            end_hrs, end_mins, end_secs = typeTimer()       # Take the time at the end.
            
            final_hrs, final_mins, final_secs = timeCalculate(  # Calculate the testing time.
                init_hrs, end_hrs, init_mins, end_mins, init_secs, end_secs
            )

            print("".join(usrInput))    # Print out user's test result in 1 string.

            finalGrade, finalPercentage, maxGrade = typeScore(  
                usrResult, sample, lostPoint
            )   # Calculate user's final grades.

            print("\n")
            print("Score: {} out of {}".format(finalGrade, maxGrade))   # Print user's grades.

            print("Accuracy: {}%".format(round(finalPercentage, 2)))    # Print the user's accuracy.

            print("Time: {}hrs, {}mins, {}secs".format(
                final_hrs,
                final_mins,
                final_secs
            ))  # Print the user's test time.

            print("Word per Minute (WPM):", typeWPM(
                usrInput,
                sampleLen,
                final_hrs,
                final_mins,
                final_secs
            ))  # Print ther user's word per minute.
            
            print("\n")

            saveLoop = True
            while (saveLoop == True):
                print("Do you want to save this record?:")
                print("(1) Yes")
                print("(2) No")
                saveInp = input("Your choice is: ")

                try:
                    int(saveInp)                # Convert input into an interger.
                    if((int(saveInp) < 1) or (int(saveInp) > 2)):   # See if the input is in range.
                        saveCheck = False
                    else:
                        if (int(saveInp) == 2): # Don't save the result if the input is 2.
                            saveCheck = False
                            saveLoop = False
                        else:
                            saveCheck = True 
                except ValueError:              #'saveCheck = False' if the input is not int.
                    saveCheck = False

                if (saveCheck == True):        # Save the result into a .txt file if the input is 1.
                    typeFileW(
                        finalGrade, maxGrade, finalPercentage, 
                        final_hrs, final_mins, final_secs,
                        usrInput, sampleLen
                    )
                    saveLoop = False
    
    print("-------------------------------------\n")