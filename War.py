import random

def war_game():
    war_game.turn = 0
    war_game.player_one_wins = False
    war_game.player_two_wins = False
    deck = [2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,11,11,11,11,12,12,12,12,13,13,13,13,14,14,14,14]
    #print(len(deck))
    deck_one = []
    deck_two = []
    while deck != []:
        random_one = random.randint(0,len(deck)-1)
        #print(random_one)
        deck_one.append(deck[random_one])
        deck.pop(random_one)

        random_two = random.randint(0,len(deck)-1)
        #print(random_two)
        deck_two.append(deck[random_two])
        deck.pop(random_two)

    #print(deck_one)
    #print(deck_two)
    #print(len(deck_one), len(deck_two))
    while deck_one != [] or deck_two != []:
        if deck_one[0] < deck_two[0]:
            #print("situation 1")
            war_game.turn += 1
            deck_two.append(deck_one[0])
            deck_one.pop(0)
            #print("TURN" + "[" + str(turn) + "]")
            #print(deck_one)
            #print(deck_two)
            if deck_one == [] or deck_two == []:
                break
            random.shuffle(deck_one)
            random.shuffle(deck_two)
        elif deck_one[0] > deck_two[0]:
            #print("situation 2")
            war_game.turn += 1
            deck_one.append(deck_two[0])
            deck_two.pop(0)
            #print("TURN" + "[" + str(turn) + "]")
            #print(deck_one)
            #print(deck_two)
            if deck_one == [] or deck_two == []:
                break
            random.shuffle(deck_one)
            random.shuffle(deck_two)
        elif deck_one[0] == deck_two[0]:
            #print("situation 3")
            if len(deck_one) > 2 and len(deck_two) > 2:
                if deck_one[2] < deck_two[2]:
                    #print("situation 4")
                    war_game.turn += 1
                    deck_two.append(deck_one[0])
                    deck_two.append(deck_one[1])
                    deck_two.append(deck_one[2])
                    #print("TURN" + "[" + str(turn) + "]")
                    #print(deck_one)
                    #print(deck_two)
                    deck_one.pop(0)
                    deck_one.pop(0)
                    deck_one.pop(0)
                    if deck_one == [] or deck_two == []:
                        break
                    random.shuffle(deck_one)
                    random.shuffle(deck_two)
                elif deck_one[2] > deck_two[2]:
                    #print("situation 5")
                    war_game.turn += 1
                    deck_one.append(deck_two[0])
                    deck_one.append(deck_two[1])
                    deck_one.append(deck_two[2])
                    #print("TURN" + "[" + str(turn) + "]")
                    #print(deck_one)
                    #print(deck_two)
                    deck_two.pop(0)
                    deck_two.pop(0)
                    deck_two.pop(0)
                    if deck_one == [] or deck_two == []:
                        break
                    random.shuffle(deck_one)
                    random.shuffle(deck_two)
                elif deck_one[2] == deck_two[2]:
                    #print("situation 6")
                    random.shuffle(deck_one)
                    random.shuffle(deck_two)
                    continue
            else:
                if deck_one == []:
                    print("Player 2 won after " + str(war_game.turn) + " turns")
                    war_game.player_two_wins = True
                    break
                else:
                    print("Player 1 won after " + str(war_game.turn) + " turns")
                    war_game.player_one_wins = True
                    break
    if deck_one == []:
        print("Player 2 won after " + str(war_game.turn) + " turns")
        war_game.player_two_wins = True
    else:
        print("Player 1 won after " + str(war_game.turn) + " turns")
        war_game.player_one_wins = True



if __name__ == "__main__":
    war_game()