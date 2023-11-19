def create_board():
    """Создаем игровое поле."""
    board = [[' ' for _ in range(3)] for _ in range(3)]
    return board


def print_board(board):
    """Выводим поле в терминал."""
    print('---------')
    for row in board:
        print('|', end='')
        for cell in row:
            print(cell, end='|')
        print('\n---------')


def make_move(board, row, col, player):
    """Ход игрока."""
    if board[row][col] == ' ':
        board[row][col] = player
        return True
    else:
        return False


def check_win(board):
    """Проверка на победу."""
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]
    return None


def is_board_full(board):
    """Проверка на заполненность поля."""
    for row in board:
        for cell in row:
            if cell == ' ':
                return False
    return True


def play_game():
    """Основная функция."""
    board = create_board()
    player = 'X'

    while True:
        print_board(board)
        print(f"Ходит игрок '{player}'")
        row = int(input("Введите номер строки (от 0 до 2): "))
        col = int(input("Введите номер столбца (от 0 до 2): "))

        if make_move(board, row, col, player):
            winner = check_win(board)
            if winner:
                print_board(board)
                print(f"Игрок '{winner}' выиграл!")
                break
            elif is_board_full(board):
                print_board(board)
                print("Мировая!")
                break
            else:
                player = 'O' if player == 'X' else 'X'
        else:
            print("Ой! Попробуйте еще раз.")


play_game()