from pathlib import Path

def typeFileR():
    while True:
        fileName = input("Please enter the file's name: ")
        
        path = Path("textSample/" + fileName + ".txt")

        if(path.is_file() == True):
            text_file = open(path,"r")
            data = text_file.read()
            text_file.close()

            return data
        else:
            print("!! FILE DOES NOT EXIST !!\n")

finalGrade, maxGrade = 1,2

def typeFileW():
     
    path = Path("textSample/record.txt")

    if(path.is_file() == True):
        text_file = open(path,"a")
        text_file.write("Score: {} out of {}".format(finalGrade, maxGrade), finalGrade, maxGrade)
        text_file.close()

    else:
        text_file = open(path,"w")
        text_file.write("Score: {} out of {}".format(finalGrade, maxGrade), finalGrade, maxGrade)
        text_file.close()

typeFileW()