import msvcrt
from datetime import *
from pathlib import Path

sampleDir = "textSample/"
recordDir = "record/"

def typeIn():
    run = 1
    userInput = []
    userResult = []
    subPoint = 0

    while (run == 1):
        pressedKey = msvcrt.getch() # Take in keyboard's input in real time.
        

        asciiCode = int(pressedKey[0])  # Convert input into ascii code.
        asciiChar = chr(pressedKey[0])  # Convert input into character.
        
        if (asciiCode == 13):   # Enter/Return to quit
            run = 0
        elif (asciiCode == 27):
            exit()
        elif(((asciiCode < 32) or (asciiCode > 126)) and (asciiCode != 8)): # Valid character check.
            subPoint += 1
            userInput.append("INVALID")
        elif(asciiCode == 8):
            if(len(userResult) > 0):
                userResult.pop()
                subPoint += 0.5
                userInput.append("<-")
            else:
                subPoint += 0.5
                userInput.append("<-")
        else:
            userInput.append(asciiChar)
            userResult.append(asciiChar)
    
    return userInput, userResult, subPoint

def typeTimer():
    now = datetime.now()

    hour = now.hour
    minute = now.minute
    second = now.second

    return hour, minute, second

def typeScore(usrInp, textInp, lostPnt):
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