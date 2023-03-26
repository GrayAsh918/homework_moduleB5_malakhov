def greet():
    print("Добро пожаловать в игру КРЕСТИКИ-НОЛИКИ!")
    print("         формат ввода: x y")
    print("         x - номер строки")
    print("         y - номер столбца")


field = [[" ", " ", " "] for i in range(3)]


def game_show():
    print(f"  0 1 2")
    for i in range(3):
        print(f"{i} {field[i] [0]} {field[i] [1]} {field[i] [2]}")


def ask():
    while True:
        x, y = map(int, input("Ваш ход:  ").split())
        if 0 <= x <= 2 and 0 <= y <= 2:
            if field[x][y] == " ":
                return x, y
            else:
                print("Клетка уже занята!")
        else:
            print("Такой клетки нет в игровом поле!")


def check_win():
    win_coord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)), ((0, 0), (1, 1), (2, 2)),
                 ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 0), (2, 0)), ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))

    for coord in win_coord:
        sym_ = []

        for c in coord:
            sym_.append(field[c[0]][c[1]])

            if sym_ == ["X", "X", "X"]:
                print(" Выиграл КРЕСТИК!")
                return True
            if sym_ == ["0", "0", "0"]:
                print(" Выиграл НОЛИК!")
                return True
    return False


num = 0

greet()

while True:
    num += 1

    game_show()

    if num % 2 == 1:
        print(" Ходит крестик ")
    else:
        print(" Ходит нолик ")

    x, y = ask()

    if num % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"

    if check_win():
        break

    if num == 9:
        print(" Ничья ")
        break
