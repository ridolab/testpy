# The fantastic game of Carta, Forbeson, Piera

from dis import Instruction
from random import randint
from time import sleep
import blessed

term = blessed.Terminal()

location_x = int(term.width/2) - 20
location_y = int(term.height/2) - 20

options = ["P", "C", "F", "X"]

message = {
  "tie": term.move_x(location_x) + "Pari, se rifá!",
  "won": term.move_x(location_x) + "Te ghe vinto!",
  "lost": term.move_x(location_x) + "Brao mona, te ghe perso!",
  "end": term.move_x(location_x) + "Zugo finio..." + term.clear() + term.home()
}

counter = {"User": 0, "Computer": 0}

instructions = [
  "- - - - - - - - - - -",
  "",
  "Premi C per Carta... F per Forbeson... P per Piera...",
  "",
  "Premi X per uscire",
  "",
  "- - - - - - - - - - -"
]


def decide_winner(user_choice, computer_choice):
  global counter

  if (user_choice in options):
    print(term.move_x(location_x) + "La scelta del Computer: %s" % (computer_choice), end="")
    print()
    if (user_choice==computer_choice):
      print (message["tie"])
    elif (user_choice==options[0] and computer_choice==options[2]):
      print (message["won"])
      counter["User"] += 1
    elif (user_choice==options[1] and computer_choice==options[0]):
      print (message["won"])
      counter["User"] += 1
    elif (user_choice==options[2] and computer_choice==options[1]):
      print (message["won"])
      counter["User"] += 1
    else:
      print (message["lost"])
      counter["Computer"] += 1
  else:
    print(term.move_x(location_x) + "Te ghe sbagliá scelta, riprova!")

def play_RPS():
  global counter
  play = True
  # clear the screen
  print(term.home + term.cadetblue1_on_bisque4 + term.clear)
  print ()
  print ("Te ste zugando al fantastico zugo: Carta, Forbeson, Piera \n")
  print ("Caricamento in corso...")
  sleep(1)
  while play :
    # clear the screen
    print(term.home + term.cadetblue1_on_bisque4 + term.clear)
    print (term.move_x(location_x) + "TI  " + str(counter["User"]), "-", str(counter["Computer"]) + "  EL COMPUTER")
    print(term.move_y(location_y))
    for line in instructions:
      print(term.move_x(location_x) + line)
    print(term.move_x(location_x) + "Ti sa dito: Carta, Forbeson, Piera: ")
    user_choice = ''
    with term.cbreak():
      user_choice = term.inkey(timeout=3)
      user_choice = user_choice.upper()
      if user_choice == options[3]:
        play = False
        print (message["end"])
        break
      computer_choice = options[randint(0, 2)]
      decide_winner(user_choice, computer_choice)
      sleep (2)

play_RPS()
