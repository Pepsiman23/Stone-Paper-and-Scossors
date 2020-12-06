from random import randrange

player_score = 0
comp_score = 0


def score():
    global player_score
    global comp_score


def game():
    global player_score
    global comp_score

    print('''Game "Stone, Paper and Scissors"
     1 - Stone
     2 - Scissors
     3 - Paper
    ''')

    while True:
        player = int(input("Choose the number: \n"))

        if player == 1:
            print("Your choice is "'Stone'"\n")
        elif player == 2:
            print("Your choice is 'Scissors'\n")
        elif player == 3:
            print("Your choice is 'Paper'\n")
        else:
            print("Wrong value\n")
            player = int(input("Choose the number: \n"))

        comp = int(randrange(3) + 1)
        if comp == 1:
            print("Machines choice is 'Stone'\n")
        if comp == 2:
            print("Machines choice is 'Scissors'\n")
        if comp == 3:
            print("Machines choice is 'Paper'\n")

        if (comp == 2 and player == 1) or (comp == 3 and player == 2) or (comp == 1 and player == 3):
            print('You won!\n')
            player_score += 1
            print("Total score: Machine - " + str(comp_score) + " Yours: " + str(player_score))
        elif (comp == 1 and player == 2) or (comp == 2 and player == 3) or (comp == 3 and player == 1):
            print('Machine won!\n')
            comp_score += 1
            print("Total score: Machine: " + str(comp_score) + " Yours: " + str(player_score))
        else:
            print('Draw!\n')
            print("Total score: Machine: " + str(comp_score) + " Yours: " + str(player_score))

        activation = input("Do you wanna play?(yes/no)")
        if activation == "yes":
            game()
        elif activation == "no":
            print("Good luck")
            exit()
        else:
            print("Did not get that")
            activation = input("Do you wanna play?(yes/no)")


game()
