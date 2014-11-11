#!/usr/bin/env python
with open('content.txt','r') as f:
    Happy = 0
    Sad = 0
    Sarcastic = 0
    Surprised = 0
    Crook = 0
    Neutral = 0
    Angry = 0
        for line in f:
            for word in line.split():       
         #  print(word)
       
        if word == ":)" or word == ":D":
            Happy = Happy + 1
        elif word == ":(" or word == ":'(" :
            Sad = Sad + 1
        elif word == ":P" or word == ";)" :
            Sarcastic = Sarcastic + 1
        elif word == ":-o" or word == "O_O" :
            Surprised = Surprised + 1
        elif word == "B-)" or word == ";)" :
            Crook = Crook + 1
        elif word == ":-/" or word == "=_=" :
            Neutral = Neutral + 1
        elif word == "x-(" or word == ">_<" :
            Angry = Angry + 1
Total = Happy + Sad + Sarcastic + Surprised + Crook + Neutral + Angry
Happy = (Happy)*(100.0/Total)
Sad = (Sad)*(100.0/Total)
Sarcastic = (Sarcastic)*(100.0/Total)
Surprised = (Surprised)*(100.0/Total)
Crook = (Crook)*(100.0/Total)
Neutral = (Neutral)*(100.0/Total)
Angry = (Angry)*(100.0/Total)
print(Happy)
print(Sad)
print(Sarcastic)
print(Surprised)
print(Crook)
print(Neutral)
print(Angry)
