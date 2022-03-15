# Name\Badr Mohamed Ragab ElSaid
# ID\ 20210605
# The Name Of The Game\ (5) one line memory game
# The idea of the game:- is that there are two players, each of whom chooses a number from one to twenty,
# and each number carries a letter of the English letters, and each letter has two copies, and the player
# that has big score win the game If the score are equal, we go to a draw.


number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
number_list_len = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

printed_list = ["Q", "E", "W", "I", "P", "U", "R", "Y", "T", "O", "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"]

global y
global player_number
global score_1
global score_2
global X

score_1 = 0
score_2 = 0

# This Funcion For Display the Game TO The players.
def display_game():

    print("welcome to my game....\nthis game is called one line memory game.....\nenjoy with this game..... ")
    print(number_list)

# This Function is check if the first player or the second is win or the two players are drawn
# and end the game
def check_win(score_1, score_2):

    if len(number_list_len) == 0:
        if score_1 > score_2:

            print("\nPlayer 1 won ! ")

        elif score_2 > score_1:

            print("\nplayer 2 won !")

        else:

            print("\nThe Game is draw ! ")

        print("\nThe Game is over :) ")
        exit()

    else:
        global y
        y += 1

# this function is increased the player score if the the two characters are the same
# and if is not the same don't increase the player score
def player_score(player_number):

    global score_1
    global score_2

    if X == 1:
        if player_number == 1:

            score_1 += 1

            print("player ", player_number, " Score = ", score_1)

        else:

            score_2 += 1

            print("player ", player_number, " Score = ", score_2)
    else:

        if player_number == 1:

            print("player ", player_number, " Score = ", score_1)

        else:

            print("player ", player_number, " Score = ", score_2)
    check_win(score_1, score_2)

# This function is handling the input and take the index of the inputs and
# show the characters in this numbers

def remove_insert(num1, num2):

    index1 = number_list.index(num1)
    index2 = number_list.index(num2)

    number_list.remove(num1)
    number_list.remove(num2)

    number_list.insert(index1, printed_list[index1])
    number_list.insert(index2, printed_list[index2])
    print(number_list)

    check(num1, num2, index1, index2)

# This function check if the 2 characters of the input is the same or not
# if the 2 characters are not the same back the numbers again and print to the user that are not the same characters
# if the 2 characters are the same we remove the number and put stars in the place
# of the 2 numbers that has the same characters
def check(num1, num2, index1, index2):
    global X

    if printed_list[index1] == printed_list[index2]:

        number_list.remove(printed_list[index1])
        number_list.remove(printed_list[index2])

        number_list_len.pop()
        number_list_len.pop()

        number_list.insert(index1, "*")
        number_list.insert(index2, "*")
        print(number_list)

        X = 1

        player_score(player_number)

    else:

        number_list.remove(printed_list[index1])
        number_list.remove(printed_list[index2])

        number_list.insert(index1, num1)
        number_list.insert(index2, num2)

        print(number_list)
        print("They are not same character ")

        X = 0

        player_score(player_number)

# This function make to handling players and if number 1 is played make him number 2  and the opposite
def player(player_number):

    if player_number == 1:
        player_number = 2

    else:
        player_number = 1

    return player_number


# This Funcion take inputs from palyers and check if the numbers from 1 to 20 or not

def players_inputs():

    global player_number



    while True:

        if y % 2 == 0:
            player_number = 1
        else:
            player_number = 2


        print("Player ", player_number, " : please enter the first number from 1 to 20 :  ")
        num1 = int(input())

        print("Player ", player_number, "please enter another number from 1 to 20:  ")
        num2 = int(input())

        while (num1 == num2):
                print("please choose different numbers ")
                print("Player ", player_number, " : please enter the first number from 1 to 20 :  ")
                num1 = int(input())

                print("Player ", player_number, "please enter another number from 1 to 20:  ")
                num2 = int(input())





        if (num1 in number_list) and (num2 in number_list) and (20 >= num1 > 0) and (20 >= num2 > 0):
            remove_insert(num1, num2)


        else:
            print("this is false numbres try again and enter number from 1 to 20")



y = 0




display_game()
players_inputs()

