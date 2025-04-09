board = [[' ' for x in range(3)] for y in range(3)]


def win_check(board):
    for row in board:
        if row[0]==row[1]==row[2]!=' ':
            return row[0]
        
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            return board[0][col]
    
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]

    return None
    

def is_full(board):
    for row in board:
        for value in row:
            if value==' ':
                return False
            
    return True

while True:
    for r in range(3):
        print(" " + board[r][0] + " | " + board[r][1] + " | " + board[r][2])
        if r != 2:
            print("---|---|---")

    x = int(input("다음 수의 x좌표를 입력하시오: "))
    y = int(input("다음 수의 y좌표를 입력하시오: "))

    if board[2-y][x] !=' ':
        print("잘못된 위치입니다.")
        continue
    else:
        board[2-y][x]='X'

    
    winner = win_check(board)
    if winner:
        print("player 승")
        break

    if is_full(board)==True:
        print("무승부")
        break



    done = False
    for i in range(3):
        for j in range(3):
            if board[i][j]==' ' and not done:
                board[i][j]='O'
                done = True
                break

    winner = win_check(board)
    if winner:
        print("computer 승")
        break







