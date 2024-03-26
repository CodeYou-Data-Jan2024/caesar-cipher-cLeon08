# add your code here
orgMsg = input("Please enter a sentence: ")
newMsg = ""

for i in range(len(orgMsg)):
    char = orgMsg[i]
    if (char.isupper()):
        newMsg += chr((ord(char) + 5-65) % 26 + 65)
    elif (char == " "):
        newMsg += char
    elif not (char.isalpha() or char.isdigit() or char == " " ):
        newMsg += char
    else:
        newMsg += chr((ord(char) + 5-97) % 26 + 97)
    
print ("The encrypted sentence is: " + newMsg.lower())