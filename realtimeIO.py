import msvcrt

run = 0

while (run == 0):
    pressedKey = msvcrt.getch()
    if (str(pressedKey) == "b'a'"):    
        print ("a was pressed")
    elif (str(pressedKey) == "b'\\r'"):
        run = 1
    else:
        print(">> ", pressedKey, pressedKey[0], chr(pressedKey[0]))

print("End")
#   pressedKey[0] will return ascii value
#   chr(pressedKey[0] will return converted ascii value