import pygame
import requests

# Making a get request to the API with the correct URL
try:
    resp = requests.get("https://sugoku.onrender.com/board?difficulty=easy")
    resp.raise_for_status()  # Check if the request was successful
except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")
    exit()

# Checking if the response is in JSON format and contains 'board'
try:
    board = resp.json().get('board')
    if not board:
        print("No board found in the response")
        exit()
except requests.exceptions.JSONDecodeError:
    print("Failed to decode JSON")
    exit()

# Make a copy of the board
original = [[board[i][j] for j in range(len(board[0]))] for i in range(len(board))]

bg_color = (250, 245, 243)
black = (0, 0, 0)

# Initialize Pygame and create a window
pygame.init()
window = pygame.display.set_mode((550, 550))
pygame.display.set_caption('Sudoku Solver')

def draw_grid():
    for i in range(0, 10):
        if i % 3 == 0:
            pygame.draw.line(window, black, (50 + 50 * i, 50), (50 + 50 * i, 500), 4)
            pygame.draw.line(window, black, (50, 50 + 50 * i), (500, 50 + 50 * i), 4)
        else:
            pygame.draw.line(window, black, (50 + 50 * i, 50), (50 + 50 * i, 500), 2)
            pygame.draw.line(window, black, (50, 50 + 50 * i), (500, 50 + 50 * i), 2)

def place_elements():
    font = pygame.font.SysFont('Arial', 30)
    for x in range(0, len(board[0])):
        for y in range(0, len(board[0])):
            if 0 < board[x][y] < 10:
                val = font.render(str(board[x][y]), True, (100, 100, 200))
                window.blit(val, ((y + 1) * 50 + 15, (x + 1) * 50 + 5))

def is_empty(pos):
    return board[pos[1]][pos[0]] == 0

def is_valid(num, pos):
    for i in range(len(board[0])):
        if board[pos[1]][i] == num and pos[0] != i:
            return False
    for i in range(len(board)):
        if board[i][pos[0]] == num and pos[1] != i:
            return False
    box_x = pos[0] // 3
    box_y = pos[1] // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False
    return True

def solve():
    find = find_empty()
    if not find:
        return True
    else:
        row, col = find
    for i in range(1, 10):
        if is_valid(i, (col, row)):
            board[row][col] = i
            if solve():
                return True
            board[row][col] = 0
    return False

def find_empty():
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)
    return None

def check_board():
    print("checking res")
    flag = 1
    for i in range(0, 9):
        if flag == 0:
            break
        l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for j in range(0, 9):
            if 0 < board[i][j] < 10 and board[i][j] in l:
                l.remove(board[i][j])
        if len(l) != 0:
            flag = 0
            break
        l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for j in range(0, 9):
            if 0 < board[j][i] < 10 and board[j][i] in l:
                l.remove(board[j][i])
        if len(l) != 0:
            flag = 0
            break
    if flag == 1:
        for x in range(0, 3):
            for y in range(0, 3):
                l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                for i in range(x * 3, x * 3 + 3):
                    for j in range(y * 3, y * 3 + 3):
                        if 0 < board[i][j] < 10 and board[i][j] in l:
                            l.remove(board[i][j])
                if len(l) != 0:
                    flag = 0
                    break
    if flag == 1:
        print('won')
    else:
        print('lost')

def main():
    window.fill(bg_color)
    draw_grid()
    place_elements()
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    solve()
                    window.fill(bg_color)
                    draw_grid()
                    place_elements()
                    pygame.display.update()
                    check_board()

main()
