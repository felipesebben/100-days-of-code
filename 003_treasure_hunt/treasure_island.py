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

# https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

# Write your code below this line 👇

crossroads = input('You\'re at a crossroad. Where do you want to go?' +
                   ' Type "left" or "right"\n').lower()

if crossroads == "left":
    # Continue in the game.
    lake = input('You\'ve come to a lake. There is an island in the middle' +
                 'of the lake. Type "wait" to wait for a boat.' +
                 ' Type "swim" to swim across.\n').lower()
    if lake == "wait":
        # Game will go on.
        house = input('You arrive at the island unharmed. ' +
                      'There is a house with 3 doors. ' +
                      'One red, one yellow and one blue. ' +
                      'Which colour do you choose?\n').lower()
        if house == "red":
            print("Burned by fire. Game over")
        elif house == 'yellow':
            print("You win!")
        elif house == "blue":
            print("Some crazy hobos kill you right away. Game over!")
        else:
            print("Game over")
    else:
        print("You forgot some jerked beef in your pocket, " +
              "and just like a family-sized salami, " +
              "you ended up being eaten by a crocodile. Game over.")
else:
    print("A bunch of cannibals invited you for dinner. Game over.")
