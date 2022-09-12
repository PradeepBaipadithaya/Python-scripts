from win32com.client import Dispatch

def speak(audio) :
      speak = Dispatch(("sapi.spvoice"))
      speak.speak(audio)

import random
list = range(100)
choice = random.choice(list)

i = 1
print("You have 10 attempts to guess the number\n")
speak("You have 10 attempts to guess the number")
speak("Please enter the number")
while(i<11) :
   guess_no = int(input("\nguess the no :\n"))
   
   if guess_no > choice :
      print("Your number is greater")
      speak("Your number is greater")
   elif guess_no < choice :
      print("Your number is less")
      speak("Your number is less")
   else :
      print("You win") 
      speak("You win")
      break     
   i = i + 1    
   print("Number of attempts remaining =",11-i)
   k = 11-i
   speak(f"You have {k} more number of attempts")

if guess_no == choice :
   print(f"You have used {i} number of attempts") 
   speak(f"You have used {i} number of attempts")
elif 11-i ==0 :
   print("You have lost all the attempts please try again")
   speak("You have lost all the attempts please try again")


