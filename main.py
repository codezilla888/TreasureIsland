print("Welcome to Treasure Island.\n"
      "Your mission is to find the treasure.")
lr = input('You\'re at a crossroad, where do ypu want to go? Type "left" or "right".')
if lr.lower() == "left":
    sw = input('You\'ve come to lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. '
               'Type "swim" to swim across')
    if sw.lower() == "wait":
        door = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one "
                     "blue. Which colour do you choose?")
        if door.lower() == "yellow":
            print("You Win!")
        else:
            print("You chose a room of beasts. Game Over.")
    else:
        print("You got attacked by an angry trout. Game Over.")
else:
    print("You fell into a hole. Game Over.")