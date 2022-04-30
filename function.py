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
    inpLen = len(usrInp)
    maxGrade = len(textInp)
    correctAns = 0

    for x in range(inpLen):
        if (usrInp[x] == textInp[x]):
            correctAns += 1

    finalGrade = correctAns - lostPnt
    finalPercentage = (finalGrade / maxGrade) * 100

    return finalGrade, finalPercentage, maxGrade

def wordCount(string):
    wordCount = 1

    for i in range(len(string)):
        if ((string[i] == ' ') or (string[i] == '\n') or (string[i] == '\t')):
            wordCount += 1
    return wordCount

def timeCalculate(init_hrs, end_hrs, init_mins, end_mins, init_secs, end_secs):
    final_hrs = end_hrs - init_hrs
    final_mins = end_mins - init_mins
    final_secs = end_secs - init_secs

    if (final_hrs < 0):
        final_hrs = 60 + final_hrs
    if (final_mins < 0):
        final_mins = 60 + final_mins
    if (final_secs < 0):
        final_secs = 60 + final_secs

    return final_hrs, final_mins, final_secs

def typeWPM(usrInp, wordCount, hrs, mins, secs):
    charCount = len(usrInp)
    minsCount = (hrs * 60) + mins + (secs * 60)

    if(minsCount == 0):
        minsCount = 1

    grossWPM = (charCount  / wordCount) / minsCount

    return round(grossWPM, 2)

def typeFileR():
    while True:
        fileName = input("\nPlease enter the file's name ('d' for default): ")
        
        path = Path(sampleDir + fileName)

        if(path.is_file() == True):
            text_file = open(path,"r")
            data = text_file.read()
            text_file.close()
            return data
        elif(fileName == "d"):
            return "Hello World"
        else:
            print("!! FILE DOES NOT EXIST !!\n")

def typeFileW(
    finalGrade, maxGrade, finalPercentage, 
    final_hrs, final_mins, final_secs,
    usrInput, sampleLen
):
    time = datetime.now()
    path = Path(recordDir + "record.txt")

    if(path.is_file() == True):
        text_file = open(path,"a")
    else:
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
    )
    text_file.close()
    print("Saved to", path)
    print("\n\n")