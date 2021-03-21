user1=input()
user2 = input()
dec1 = input()
dec2 = input()

if(dec1 == "Rock"):
    if(dec2 == "Scissor"):
        print(user1+" Win")
    elif(dec2 == "Paper"):
        print(user2+" Win")
elif(dec1 == "Scissor"):
    if(dec2 == "Rock"):
        print(user2+" Win")
    elif(dec2 == "Paper"):
        print(user1+" Win")
else:
    if(dec2=="Rock"):
        print(user1+" Win")
    else:
        print(user2+" Win")
