# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
maps = [1,2,3,
        4,5,6,
        7,8,9]
victories = [[0,1,2],
             [3,4,5],
             [6,7,8],
             [0,3,6],
             [1,4,7,],
             [2,5,8],
             [0,4,8],
             [2,4,6]]
def print_maps():
    print(maps[0], end = " ")
    print(maps[1], end=" ")
    print(maps[2])

    print(maps[3], end=" ")
    print(maps[4], end=" ")
    print(maps[5])

    print(maps[6], end=" ")
    print(maps[7], end=" ")
    print(maps[0])
    def step_maps(step,symbol):
        ind = maps.index(step)
        maps[ind] = symbol
        def get_result():
            for i in victories:
                if maps[i[0]] =="X" and maps[i[1]] == "X" and maps[i[2]] == "X":
                    win= "X"
                    if maps[i[0]] =="O" and maps[i[1]] == "O" and maps[i[2]] == "O":
                        win = "O"

                     return win

                    game_over = False
                player1 = True

            while game_over == False:

                print_maps()

                if player1 == True:
                    symbol = "X"
                    step = int(input("Человек 1, Ваш ход: "))
                else:
                    symbol = "0"
                    step = inp(input("Человек 2, Ваш ход: "))

                    step_maps(step,symbol)
                    win = get_result()
                    if win != "":
                        game_over = True
                    else:
                        game_over = False

                        player1 = not(player1)

                        print_maps()
                        print("Победил", win)





