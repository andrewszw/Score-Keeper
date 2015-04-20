import os

def printScore(players):
    """ Prints the current score """
    os.system('clear')
    for x in players:
        print()
        print(x[0] + ": " + str(x[1]))
        print()
        print("------------------------------")


def printUse():
    """ Print use """
    print()
    print("Welcome, to THE score keeper")
    print("Follow the instructions as given.")
    print("To end the game, type 'exit'.")
    print()

def run_game(players):
    name = ""
    # run the main loop of the game while exit has not been entered
    while name != "exit":
        name = input("Player's score to update or exit: ").lower()
        if name == "exit":
            break;
        score = int(input("Number to add to score: "))
        for item in players:
            if item[0] == name:
                item[1] = item[1] + score
        printScore(players)
    print()
    print("------------------------------");
    print()
    print("Game over! The final score is as follows: ")
    printScore(players)
    
def main(): 
    printUse()

    # get the number of players
    num_players = int(input("Please enter the number of players: "))
    
    # variables to help with adding players to player list
    player_list = []
    count = 0
    score = 0
    # add the players to the list
    while count < num_players:
        tmp_list = [input("Enter a player's name: ").lower(), score]
        player_list.append(tmp_list)
        count = count + 1
    run_game(player_list)

main()
