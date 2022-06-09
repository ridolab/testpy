# The fantastic game of Carta, Forbeson, Piera

from random import randint
from time import sleep

options = ["P", "C", "F", "X"]

message = {
  "tie": "Pari! Non te ghe vinto!",
  "won": "Te ghe vinto!",
  "lost": "Brao mona, te ghe perso!",
  "end": "Zugo finio... \n "
}

def decide_winner(user_choice, computer_choice):

  print ("La scelta del Computer: %s" % (computer_choice))
  print()
  
  if (user_choice!=options[0] and user_choice!=options[1] and user_choice!=options[2] and user_choice!=options[3]):
    print("Te ghe sbaglia scelta!")  
  elif (user_choice==computer_choice):
    print (message["tie"])
  elif (user_choice==options[0] and computer_choice==options[2]):
    print (message["won"])
  elif (user_choice==options[1] and computer_choice==options[0]):
    print (message["won"])
  elif (user_choice==options[2] and computer_choice==options[1]):
    print (message["won"])
  else:
    print (message["lost"])

def play_RPS():
  play = True
  print ()
  print ("Te ste zugando al fantastico zugo: Carta, Forbeson, Piera \n")
  print ("Caricamento in corso...")
  sleep(5)
  print ("- - - - - - - - - -")
  print ("Premi C per Carta... F per Forbeson... P per Piera...")
  print ()
  print ("Premi X per uscire")
  print ("- - - - - - - - - -")  
  while play :   
    user_choice = input("Ti sa dito: Carta, Forbeson, Piera: ")
    print ()
    user_choice = user_choice.upper()
    if user_choice == options[3]:
        play = False
        print (message["end"])
        break
    computer_choice = options[randint(0, 2)]
    decide_winner(user_choice, computer_choice)
    print("- - - - - - - - - -")
    sleep (3)
play_RPS()
