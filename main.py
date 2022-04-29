### TO DO LIST:
    # Comments

from datetime import *
from pickle import TRUE
from function import *
import msvcrt


print("\n------------ TYPING TEST ------------")
print("-------------------------------------\n")

while True:
    print("Please choose the following options:")
    print("(1) Quick start")
    print("(2) Custom test")
    print("(3) Quit")

    menuInp = input("Your choice is: ")

    try:
        int(menuInp)
        if((int(menuInp) < 1) or (int(menuInp) > 3)):
            inpCheck = False
        else:
            if (int(menuInp) == 3):
                exit()
            else:
                inpCheck = True
    except ValueError:
        inpCheck = False

    if (inpCheck == True):
        if not menuInp:
            inpCheck = False

        if (int(menuInp) == 1):
            sample = "Hello World"
        elif(int(menuInp) == 2):
            sample = typeFileR()

        print("\n")
        print("Your text are:\n")
        print (sample)
        print("\n")

        print("-- Press any key to start or 'x' to quit --\n")
        pressedKey = msvcrt.getch()
        if (pressedKey[0] == 120):
            inpCheck = False
        else:
            print("GO...\n")
            sampleLen = wordCount(sample)
            init_hrs, init_mins, init_secs = typeTimer()
            usrInput, usrResult, lostPoint = typeIn()
            end_hrs, end_mins, end_secs = typeTimer()
            
            final_hrs, final_mins, final_secs = timeCalculate(
                init_hrs, end_hrs, init_mins, end_mins, init_secs, end_secs
            )

            print("".join(usrInput))

            finalGrade, finalPercentage, maxGrade = typeScore(
                usrResult, sample, lostPoint
            )

            print("\n")
            print("Score: {} out of {}".format(finalGrade, maxGrade))

            print("Accuracy: {}%".format(round(finalPercentage, 2)))

            print("Time: {}hrs, {}mins, {}secs".format(
                final_hrs,
                final_mins,
                final_secs
            ))

            print("Word per Minute (WPM):", typeWPM(
                usrInput,
                sampleLen,
                final_hrs,
                final_mins,
                final_secs
            ))
            print("\n")

            saveLoop = True
            while (saveLoop == True):
                print("Do you want to save this record?:")
                print("(1) Yes")
                print("(2) No")
                saveInp = input("Your choice is: ")

                try:
                    int(saveInp)
                    if((int(saveInp) < 1) or (int(saveInp) > 2)):
                        saveCheck = False
                    else:
                        if (int(saveInp) == 2):
                            saveCheck = False
                            saveLoop = False
                        else:
                            saveCheck = True 
                except ValueError:
                    saveCheck = False

                if (saveCheck == True):
                    typeFileW(
                        finalGrade, maxGrade, finalPercentage, 
                        final_hrs, final_mins, final_secs,
                        usrInput, sampleLen
                    )
                    saveLoop = False
    
    print("-------------------------------------\n")