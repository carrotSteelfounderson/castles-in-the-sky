import random, sys
 # create a dictionary of the possible moves and randomly select the damage it does when selected
moves = {"laser blaster": random.randint(18, 25),
         "missile battery": random.randint(10, 35),
         "repair": random.randint(20, 25),}
def isnumber(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
def main():
    go = 0
    print('you will fight')

    print('''How to fight.

ships choose a weapon . weapons can either deal moderate damage
over a low range, deal high damage but over a wide
range, or they can repair. (Note: Attacks can miss, including repair!)

Each ship starts with 100 health, and the first
player to reduce their opponent to 0 is the winner.
That's it! Good luck''')


    while True:
        winner = None
        player_health = 100
        if 'magnetic disintegrator' in moves:
            computer_health = 90
        else:
            computer_health = 100

        # determine whose turn it is
        turn = random.randint(1,2) # heads or tails
        if turn == 1:
            player_turn = True
            computer_turn = False
            print("\nthe Player will go first.")
        else:
            player_turn = False
            computer_turn = True
            print("\nthe Enemy will go first.")


        print("\nPlayer health: ", player_health, "enemy health: ", computer_health)

        # set up the main game loop
        while (player_health != 0 or computer_health != 0):

            heal_up = False # determine if heal has been used by the player. Resets false each loop.
            miss = False # determine if the chosen move will miss.

           

            if player_turn:
                print("\nPlease select a move:\n1. laser blaster (Deal damage between 18-25 unless you have beam lensing which adds five damage)\n2. missile battery (Deal damage between 10-35)\n3. repair (Restore between 20-25 health)\n")
                player_move = input("> ").lower()
                if not 'motion tracking' in moves:
                    move_miss = random.randint(1,6) # 20% of missing
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
                            player_move = moves["laser blaster"]
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


                if miss:
                    computer_move = 0 # the computer misses and deals no damage
                    print("The enemy missed!")
                else:
                    if computer_health > 30: 
                        if player_health > 75:
                            computer_move = moves["laser blaster"]
                            print("\nThe enemy used laser blaster. It dealt ", computer_move, " damage.")
                        elif player_health > 35 and player_health <= 75: # computer decides whether to go big or play it safe
                            if 'electro-pulse' not in moves:
                                imoves = ["laser blaster", "missile battery"]
                                imoves = random.choice(imoves)
                                computer_move = moves[imoves]
                                print("\nThe computer used ", imoves, ". It dealt ", computer_move, " damage.")
                            else:
                                computer_move = moves["laser blaster"]
                                print("\nThe enemy used laser blaster. It dealt ", computer_move, " damage.")
                        elif player_health <= 35:
                            if 'electro-pulse' not in moves:
                                computer_move = moves["missile battery"] # FINISH HIM!
                                print("\nThe enemy used missile battery. It dealt ", computer_move, " damage.")
                            else:
                                computer_move = moves["laser blaster"]
                                print("\nThe enemy used laser blaster. It dealt ", computer_move, " damage.")
                    else: # if the computer has less than 30 health, there is a 50% chance they will heal
                        heal_or_fight = random.randint(1,2) 
                        if heal_or_fight == 1:
                            heal_up = True
                            computer_move = moves["repair"]
                            print("\nThe enemy used repair. It repaired ", computer_move, " damage.")
                        else:
                            if player_health > 75:
                                computer_move = moves["laser blaster"]
                                print("\nThe enemy used laser blaster. It dealt ", computer_move, " damage.")
                            elif player_health > 35 and player_health <= 75:
                                if 'electro-pulse' not in moves:
                                    imoves = ["laser blaster", "missile battery"]
                                    imoves = random.choice(imoves)
                                    computer_move = moves[imoves]
                                    print("\nThe computer used ", imoves, ". It dealt ", computer_move, " damage.")
                                else:
                                    computer_move = moves["laser blaster"]
                                    print("\nThe enemy used laser blaster. It dealt ", computer_move, " damage.")
                            elif player_health <= 35:
                                if 'electro-pulse' not in moves:
                                    computer_move = moves["missile battery"]# FINISH HIM!
                                    print("\nThe enemy used missile battery. It dealt ", computer_move, " damage.")
                                else:
                                    computer_move = moves["laser blaster"]
                                    print("\nThe enemy used laser blaster. It dealt ", computer_move, " damage.")

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
                    if computer_health < 0:
                        computer_health = 0 # cap minimum health at 0
                        winner = "Player"
                        break
                else:
                    player_health -= computer_move
                    if player_health < 0:
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
            False
            break
        else:
            print("\nPlayer health: ", player_health, "Computer health: ", computer_health)
            print("\nSorry, but your opponent wiped the floor with you. Better luck next time.")
            sys.exit()
main()
