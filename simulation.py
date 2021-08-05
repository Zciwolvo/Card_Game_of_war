from War import war_game


def simulation():
    counter = 100
    divisor = counter
    score = 0
    game_count = 0
    player_one_wins = 0
    player_two_wins = 0
    while counter > 0:
        game_count += 1
        print("Game number: " + str(game_count))
        war_game()
        score += war_game.turn
        counter -= 1
        if war_game.player_one_wins == True:
            player_one_wins += 1
        elif war_game.player_two_wins == True:
            player_two_wins += 1

    final_score = score/divisor
    print("===============================================")
    print("Average card game of war takes " + str(final_score) + " turns")
    print("Player one has won " + str(player_one_wins) + " times")
    print("Player two has won " + str(player_two_wins) + " times")
    print("===============================================")


if __name__ == "__main__":
    simulation()