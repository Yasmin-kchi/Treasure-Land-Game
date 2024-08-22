

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

answer1 = input('you\'re at a cross road. where do you want to go? type "left" or "right"\n').lower()
#print(answer1)

if answer1 == "left":
    answer2 = input('Now, what do you do? type "Swim" or "Wait"\n').lower()
    #print(answer2)
    if answer2 == "Wait":
        answer3 = input('which door do you choose? Type "Red" or ""Blue" or "Yellow"\n').lower()
        #print(answer3)
        if answer3 == "Red":
           print("You were burned by fire. Game Over.")
        elif answer3 == "Blue":
            print("You were eaten by beasts. Game Over.")
        elif answer3 == "Yellow":
            print("You win!")
        else:
            print("Game Over.")
    else:
        print("You were attacked by trout. Game Over.")       
else:
    print("You fell into a hole. Game Over.")

### more atracive:(by chatGPT)
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission, should you choose to accept it, is to find the hidden treasure.") 

answer1 = input('You\'re standing at a crossroad shrouded in mystery. Left leads to the Whispering Woods, right to the Cursed Caverns. Which path calls to you? Whisper "left" or shout "right".\n').lower()

if answer1 == "left":
    answer2 = input('Ah, the Woods! A place where shadows dance and trees whisper secrets of the ancient. Ahead, a murky river blocks your path. Do you dare to swim across, or wait for the unseen bridge? Whisper "Swim" to dive into the unknown or "Wait" to trust in patience.\n').lower()
    if answer2 == "wait":
        answer3 = input('Patience reveals the bridge and across it, a mystical castle with three doors: one red as the setting sun, one blue as the deepest ocean, and one yellow as the morning sun. Which door holds your destiny? Murmur "Red", "Blue", or "Yellow".\n').lower()
        if answer3 == "red":
            print("A fiery blaze engulfs the room as the door creaks open. Game Over, brave soul.")
        elif answer3 == "blue":
            print("Monstrous beasts lurk behind the door, sealing your fate. Game Over, adventurer.")
        elif answer3 == "yellow":
            print("Golden light floods the room. Congratulations, the treasure is yours!")
        else:
            print("A mysterious force whisks you away. Game Over.")
    else:
        print("The river's creatures drag you into the depths. Game Over.")
else:
    print("The ground crumbles beneath you, and darkness consumes you. Game Over.")
