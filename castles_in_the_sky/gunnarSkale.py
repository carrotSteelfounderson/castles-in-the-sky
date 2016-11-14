import random, sys
 # create a dictionary of the possible moves and randomly select the damage it does when selected
moves = {"laser blaster": random.randint(18, 25),
         "missile battery": random.randint(10, 35),
         "repair": random.randint(20, 25),}
def main():
    go = 0
    print('''you will fight GUNNAR SKALE, legendary shadow king, whose reign of terror
has extended for thousands of years, yea even tens of thousands.
know now that fight him means pitting yourself against a wily enemy against whom
one cannot win''')

    print("\nHow to fight.\n\nships take turns to choose a weapon . weapons can either deal moderate damage")
    print("over a low range, deal high damage but over a wide")
    print("""range, or they can repair. (Note: Moves can miss, including repair!)
please take note that among his arsenal gunnar skale has constructed
a device named an EMP. this prevents all energy management.""")

    print("\nEach ship starts with 100 health, and the first")
    print("player to reduce their opponent to 0 is the winner.")

    print("\nThat's it! Good luck")
    x = True
    laser = None
    missile = None
    repair = None

    # Set up the play again loop
    while x == True:
        winner = None
        player_health = 100
        if 'magnetic disintegrator' in moves:
            computer_health = 100
        else:
            computer_health = 110

        
        player_turn = False
        computer_turn = True
        print("\nGunnar Skale will go first.")


        print("\nPlayer health: ", player_health, "Skale health: ", computer_health)

        # set up the main game loop
        while (player_health != 0 or computer_health != 0):

            heal_up = False # determine if heal has been used by the player. Resets false each loop.
            miss = False # determine if the chosen move will miss.

           

            if player_turn:
                print("\nPlease select a move:\n1. laser blaster (Deal damage between 18-25 unless you have beam lensing which adds five damage)\n2. missile battery (Deal damage between 10-35)\n3. repair (Restore between 20-25 health)\n")

                player_move = input("> ").lower()
                
                if not 'motion tracking' in moves:
                    move_miss = random.randint(1,5) # 20% of missing
                    if move_miss == 1:
                        miss = True
                    else:
                        miss = False

                if miss:
                    player_move = 0 # player misses and deals no damage
                    print("You missed!")
                else:
                    if player_move in ("1", "laser blaster"):
                        if 'beam lensing' in moves:
                            player_move = moves["laser blaster"] + 5
                        else:
                            player_move = moves["laser blaster"]
                        print("\nYou used laser blaster. It dealt ", player_move, " damage.")
                    elif player_move in ("2", "missile battery"):
                        player_move = moves["missile battery"]
                        print("\nYou used missile battery. It dealt ", player_move, " damage.")
                    elif player_move in ("3", "repair"):
                        heal_up = True # heal activated
                        player_move = moves["repair"]
                        print("\nYou used repair. It repaired ", player_move, " damage.")
                    else:
                        print("\nThat is not a valid move. Please try again.")
                        continue

            else: # computer turn

                if 'chaff' not in moves:
                    move_miss = random.randint(1,5)
                else:
                    move_miss = random.randint(1,3)
                if move_miss == 1:
                    miss = True
                else:
                    miss = False

                if miss:
                    computer_move = 0 # the computer misses and deals no damage
                    print("Gunnar skale missed!")
                else:
                    if laser == None:
                        computer_move = moves["laser blaster"]
                        print("\nGunnar Skale used laser blaster. It dealt ", computer_move, " damage.")
                        laser = computer_move
                    elif missile == None and 'electro-pulse' not in moves:
                        computer_move = moves["missile battery"] # FINISH HIM!
                        print("\nGunnar Skale used missile battery. It dealt ", computer_move, " damage.")
                        missile = computer_move
                    elif repair == None:
                        heal_up = True
                        computer_move = moves["repair"]
                        print("\nGunnar Skale used repair. It repaired ", computer_move, " damage.")
                        repair = computer_move
                    else:
                        if missile != None and missile > laser:
                            high = 'missile battery'
                        else:
                            high = 'laser blaster'
                        if computer_health - moves[high] <= 10:
                            heal_up = True
                            computer_move = moves["repair"]
                            print("\nGunnar Skale used repair. It repaired ", computer_move, " damage.")
                            repair = computer_move
                        else:
                            computer_move = moves[high]
                    
                        
            if heal_up:
                if player_turn:
                    player_health += player_move
                    if player_health > 100:
                        player_health = 100 # cap max health at 100. No over healing!
                else:
                    computer_health += computer_move
                    if computer_health > 100:
                        computer_health = 100
            else:
                if player_turn:
                    computer_health -= player_move
                    if computer_health <= 15:
                        if computer_health <= 0:
                            computer_health = 0 # cap minimum health at 0
                            winner = "Player"
                            break
                        else:
                            winner = 'none'
                            break
                else:
                    player_health -= computer_move
                    if player_health <= 0:
                        player_health = 0
                        winner = "Computer"
                        break

            print("\nPlayer health: ", player_health, "Computer health: ", computer_health)

            # switch turns
            if 'rapid fire' in moves:
                if player_turn:
                    go += 1
                if computer_turn or go == 2:
                    player_turn = not player_turn
                    computer_turn = not computer_turn
                    go = 0
            else:    
                player_turn = not player_turn
                computer_turn = not computer_turn

        # once main game while loop breaks, determine winner and congratulate

        if winner == "Player":
            print("\nPlayer health: ", player_health, "Computer health: ", computer_health)
            print("\nCongratulations! You have won. You're an animal!!")
            x = False
        elif winner == "computer":
            print("\nPlayer health: ", player_health, "Computer health: ", computer_health)
            print('''\nSorry, but tonight GUNNAR SKALE, legendary shadow king, whose reign of terror
has extended for thousands of years, yea even tens of thousands will
rejoice in your death and those of oh so many others. Better luck next
time.''')
            sys.exit()
        else:
            print("\nPlayer health: ", player_health, "Computer health: ", computer_health)
            print('GUNNAR escaped, but with your strength and courage, he can surely be defeated')
        x = False

