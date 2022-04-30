import msvcrt
from datetime import *
from pathlib import Path

sampleDir = "textSample/"
recordDir = "record/"

def typeIn():       # The typing test itself.
    run = 1
    userInput = []  # List to hold user's input.
    userResult = [] # List to hold sample text.
    subPoint = 0    # Point deducted.

    while (run == 1):
        pressedKey = msvcrt.getch() # Take in keyboard's input in real time.
        

        asciiCode = int(pressedKey[0])  # Convert input into ascii code.
        asciiChar = chr(pressedKey[0])  # Convert input into character.
        
        if (asciiCode == 13):   # Enter/Return to end the test.
            run = 0
        elif (asciiCode == 27): # Esc to quit the program.
            exit()
        elif(((asciiCode < 32) or (asciiCode > 126)) and (asciiCode != 8)): # Valid character check.
            subPoint += 1                                                   # Deduct point.
            userInput.append("INVALID")
        elif(asciiCode == 8):           # Check if user hit backspace.
            if(len(userResult) > 0):
                userResult.pop()        # Pop the last character if the list is not empty.
                subPoint += 0.5         # Deduct point.
                userInput.append("<-")  # Append 'backspace' into the user's list.
            else:
                subPoint += 0.5         # Deduct point.
                userInput.append("<-")  # Append 'backspace' into the user's list.
        else:
            userInput.append(asciiChar)     # Append all user's input including backspace.
            userResult.append(asciiChar)    # Doesn't append backspace and popped characters.
    
    return userInput, userResult, subPoint

def typeTimer():    # To get the current time on call.
    now = datetime.now()    # Get the current time and put it in 'now' object.

    hour = now.hour         # Get the current hour from 'now' and put it in 'hour'
    minute = now.minute     # Get the current minute from 'now' and put it in 'minute'
    second = now.second     # Get the current second from 'now' and put it in 'second'

    return hour, minute, second

def typeScore(usrInp, textInp, lostPnt):    # Calculate the final percentage and score.
    inpLen = len(usrInp)                    # Get lenght of user's input.
    maxGrade = len(textInp)                 # Get lenght of sample text.
    correctAns = 0

    for x in range(inpLen):
        if (usrInp[x] == textInp[x]):       # Compare user's input and sample.
            correctAns += 1                 # +1 score everytime the character match.

    finalGrade = correctAns - lostPnt               # Subtrack points from 'backspace', etc.
    finalPercentage = (finalGrade / maxGrade) * 100 # Get the final percentage of the score.

    return finalGrade, finalPercentage, maxGrade

def wordCount(string):  # Count how many words in the user's sample .txt.
    wordCount = 1

    for i in range(len(string)):    # Go through the file, to find space, new line and tab. 
        if ((string[i] == ' ') or (string[i] == '\n') or (string[i] == '\t')):
            wordCount += 1          # Increament the word count.
    return wordCount

def timeCalculate(init_hrs, end_hrs, init_mins, end_mins, init_secs, end_secs): # Find the time.
    final_hrs = end_hrs - init_hrs      # Get the hours different before and after texting.
    final_mins = end_mins - init_mins   # Get the minutes different before and after texting.
    final_secs = end_secs - init_secs   # Get the seconds different before and after texting.

    if (final_hrs < 0):                 # If the result is negative number, add 60 to it.
        final_hrs = 60 + final_hrs
    if (final_mins < 0):
        final_mins = 60 + final_mins
    if (final_secs < 0):
        final_secs = 60 + final_secs

    return final_hrs, final_mins, final_secs

def typeWPM(usrInp, wordCount, hrs, mins, secs):    # Calculate word per minute.
    charCount = len(usrInp)
    minsCount = (hrs * 60) + mins + (secs * 60)     # Convert everything to minute.

    if(minsCount == 0):                             # Set minute = 1 to prevent divisor = 0.
        minsCount = 1

    grossWPM = (charCount  / wordCount) / minsCount # Gross WPM formula.

    return round(grossWPM, 2)

def typeFileR():    # Take in user's sample .txt file.
    while True:
        fileName = input("\nPlease enter the file's name ('d' for default): ")
        
        path = Path(sampleDir + fileName)   # Combine user's input and the default dir.

        if(path.is_file() == True):         # Check if the file is exist.
            text_file = open(path,"r")      # Open the file.
            data = text_file.read()         # Read the file into data.
            text_file.close()               # Close the file.
            return data
        elif(fileName == "d"):              # Return default sample if user input 'd'.
            return "Hello World"
        else:                               # File does not exist.
            print("!! FILE DOES NOT EXIST !!\n")

def typeFileW(
    finalGrade, maxGrade, finalPercentage, 
    final_hrs, final_mins, final_secs,
    usrInput, sampleLen
):                                          # Save the testing record into a .txt file.
    time = datetime.now()                   # Get current time.
    path = Path(recordDir + "record.txt")   # Get the path of the record.txt file

    if(path.is_file() == True):             # If the file existed, append to it.
        text_file = open(path,"a")
    else:                                   # If the file doesn't exist, create and write to it.
        text_file = open(path,"w")

    text_file.write(
        "Date: {}\nScore: {} out of {}\nAccuracy: {}%\nTime: {}hrs, {}mins, {}secs\nWord per Minute (WPM): {}\n\n"
        .format(
            time,
            finalGrade, maxGrade,
            round(finalPercentage, 2),
            final_hrs, final_mins, final_secs,
            typeWPM(usrInput, sampleLen, final_hrs, final_mins, final_secs)
        )
    )                       # Write in everything needed to be record.
    text_file.close()       # Close the file.
    print("Saved to", path) # Prompt the user that everything is saved.
    print("\n\n")