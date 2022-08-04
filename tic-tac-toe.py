import pygame
import os
import random
import time

WIDTH, HEIGHT = 1280, 1000

GAME = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

WHITE = (255, 255, 255)
FPS = 60

grid_width = 500
grid_height = 500

width = 130
height =  130

grid_image = pygame.image.load(os.path.join("media", "grid.png"))
grid = pygame.transform.scale(grid_image, (grid_width, grid_height))

circle_image = pygame.image.load(os.path.join("media", "circle.png"))
mark_image = pygame.image.load(os.path.join("media", "mark.png"))

circles = []
marks = []
coordinates_circles = []
coordinates_marks = []

PLACED_CIRCLES = -1
PLACED_MARKS = -1

grid_x = WIDTH / 2 - 250
grid_y = HEIGHT / 2 - 250

grid_matrix = [
    [0, 0, 0], 
    [0, 0, 0],
    [0, 0, 0]
]

for i in range(5):
    coordinates_circles.append([-200, -200]) 
for i in range(5):
    coordinates_marks.append([-200, -200]) 


for i in range(5):
    circles.append(pygame.transform.scale(circle_image, (width, height))) 
    marks.append(pygame.transform.scale(mark_image, (width, height)))  


def draw_window():
    GAME.fill(WHITE)
    GAME.blit(grid, (grid_x, grid_y))
    for i in range(5):
        GAME.blit(circles[i], (coordinates_circles[i][0], coordinates_circles[i][1]))
        GAME.blit(marks[i - 5], (coordinates_marks[i][0], coordinates_marks[i][1]))
    
    pygame.display.update()

def place(element, x, y):
    global PLACED_CIRCLES, PLACED_MARKS
    if element == "circle":
        PLACED_CIRCLES += 1
        coordinates_circles[PLACED_CIRCLES][0] = grid_x + (x - 1) * (grid_width / 3) + 20
        coordinates_circles[PLACED_CIRCLES][1] = grid_y + (y - 1) * (grid_height / 3) + 20
        grid_matrix[x - 1][y - 1] = 1
    else:
        PLACED_MARKS += 1
        coordinates_marks[PLACED_MARKS][0] = grid_x + (x - 1) * (grid_width / 3) + 20
        coordinates_marks[PLACED_MARKS][1] = grid_y + (y - 1) * (grid_height / 3) + 20
        grid_matrix[x - 1][y - 1] = 2
    
    print(grid_matrix)


def main():
    clock = pygame.time.Clock()
    run = True
    turn = 0
     
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                run = False
        x_mouse, y_mouse = pygame.mouse.get_pos()
            
        if pygame.mouse.get_pressed()[0]:
            time.sleep(0.1)
            if x_mouse > grid_x and x_mouse < grid_x + grid_width and y_mouse > grid_y and y_mouse < grid_y + grid_height:
                # first column
                if x_mouse < grid_x + grid_width / 3:
                    # 1 row
                    if y_mouse < grid_y + grid_height / 3:
                        print("you clicked position 1, 1")
                        if turn == 0 and grid_matrix[0][0] == 0:
                            place("circle", 1, 1)
                            turn = 1
                            print("circle placed")
                        elif turn == 1 and grid_matrix[0][0] == 0:
                            place("mark", 1, 1)
                            turn = 0
                            print("marks placed")
                    # 2 row
                    elif y_mouse < grid_y + 2 * (grid_height / 3) and y_mouse > grid_y + grid_height / 3:
                        print("you clicked position 1, 2")
                        if turn == 0 and grid_matrix[0][1] == 0:
                            place("circle", 1, 2)
                            turn = 1
                            print("circle placed")
                        elif turn == 1 and grid_matrix[0][1] == 0:
                            place("mark", 1, 2)
                            turn = 0
                            print("marks placed")
                    # 3 row
                    else:
                        print("you clicked position 1, 3")
                        if turn == 0 and grid_matrix[0][2] == 0:
                            place("circle", 1, 3)
                            turn = 1
                            print("circle placed")
                        elif turn == 1 and grid_matrix[0][2] == 0:
                            place("mark", 1, 3)
                            turn = 0
                            print("marks placed")
                
                # second column 
                elif x_mouse > grid_x + grid_width / 3 and x_mouse < grid_x + 2 * (grid_width / 3):
                    # 1 row
                    if y_mouse < grid_y + grid_height / 3:
                        print("you clicked position 2, 1")
                        if turn == 0 and grid_matrix[1][0] == 0:
                            place("circle", 2, 1)
                            turn = 1
                            print("circle placed")
                        elif turn == 1 and grid_matrix[1][0] == 0:
                            place("mark", 2, 1)
                            turn = 0
                            print("marks placed")
                    # 2 row
                    elif y_mouse < grid_y + 2 * (grid_height / 3) and y_mouse > grid_y + grid_height / 3:
                        print("you clicked position 2, 2")
                        if turn == 0 and grid_matrix[1][1] == 0:
                            place("circle", 2, 2)
                            turn = 1
                            print("circle placed")
                        elif turn == 1 and grid_matrix[1][1] == 0:
                            place("mark", 2, 2)
                            turn = 0
                            print("marks placed")
                    # 3 row
                    else:
                        print("you clicked position 2, 3")
                        if turn == 0 and grid_matrix[1][2] == 0:
                            place("circle", 2, 3)
                            turn = 1
                            print("circle placed")
                        elif turn == 1 and grid_matrix[1][2] == 0:
                            place("mark", 2, 3)
                            turn = 0
                            print("marks placed")
                
                # third column
                else:
                    # 1 row
                    if y_mouse < grid_y + grid_height / 3:
                        print("you clicked position 3, 1")
                        if turn == 0 and grid_matrix[2][0] == 0:
                            place("circle", 3, 1)
                            turn = 1
                            print("circle placed")
                        elif turn == 1 and grid_matrix[2][0] == 0:
                            place("mark", 3, 1)
                            turn = 0
                            print("marks placed")
                    # 2 row
                    elif y_mouse < grid_y + 2 * (grid_height / 3) and y_mouse > grid_y + grid_height / 3:
                        print("you clicked position 3, 2")
                        if turn == 0 and grid_matrix[2][1] == 0:
                            place("circle", 3, 2)
                            turn = 1
                            print("circle placed")
                        elif turn == 1 and grid_matrix[2][1] == 0:
                            place("mark", 3, 2)
                            turn = 0
                            print("marks placed")
                    # 3 row
                    else:
                        print("you clicked position 3, 3")
                        if turn == 0 and grid_matrix[2][2] == 0:
                            place("circle", 3, 3)
                            turn = 1
                            print("circle placed")
                        elif turn == 1 and grid_matrix[2][2] == 0:
                            place("mark", 3, 3)
                            turn = 0
                            print("marks placed")
        draw_window()

    pygame.quit()

if __name__ == "__main__":
    main()
    