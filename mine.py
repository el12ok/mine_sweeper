import random
field = []
width = 3 
height = 3 
bomb_numbers = 2
bomb_icon = 9
x_bomb = 0
y_bomb = 0

from pprint import pprint
for i in range(height):
    field.append([])
    for j in range(width):
        field[i].append(0)

for i in range(bomb_numbers): 
    x_bomb = random.randint(0,width-1)
    y_bomb = random.randint(0, height-1)
    while field[y_bomb][x_bomb] == bomb_icon:
        x_bomb = random.randint(0,width-1)
        y_bomb = random.randint(0, height-1)
    field[y_bomb][x_bomb] = bomb_icon
 
for i in range(height):
    for j in range(width):
        if field[i][j] == bomb_icon:
            continue
        if i-1>=0 and j-1>=0 and field[i-1][j-1] == bomb_icon: 
            field[i][j] += 1
        if i-1>=0 and field[i-1][j] == bomb_icon: 
            field[i][j] += 1 
        if i-1>=0 and j+1<=width-1 and field[i-1][j+1] == bomb_icon: 
            field[i][j] += 1 
        if j-1>=0 and field[i][j-1] == bomb_icon:
            field[i][j] += 1 
        if j+1<=width-1 and field[i][j+1] == bomb_icon:
            field[i][j] += 1 
        if i+1<=height-1 and j-1>=0 and field[i+1][j-1] == bomb_icon:
            field[i][j] += 1 
        if i+1<=height-1 and field[i+1][j] == bomb_icon:
            field[i][j] += 1 
        if i+1<=height-1 and j+1<=width-1 and field[i+1][j+1] == bomb_icon:
            field[i][j] += 1 
            
# horizontal_pattern = "---*"
# vertical_pattern = " |"
# line = "*" + horizontal_pattern*width
# for i in range(height):
#     print(line)
#     print("|", end = "")
#     for j in range(width): 
#         if field[i][j] == 0:
#             print("  " + vertical_pattern, end = "")
#         else: 
#             print(" ", field[i][j], vertical_pattern, sep = "", end = "")
#     #print("|" + vertical_pattern*width)
#     print()
# print(line)

click_field = []
for i in range(height):
    click_field.append([])
    for j in range(width):
        click_field[i].append(0)
        

while True: 
    pos_x, pos_y = input(("Enter coordinates x&y: ")).split()
    pos_x = int(pos_x)-1
    pos_y = int(pos_y)-1
    if field[pos_y][pos_x] == bomb_icon:
        print("Game over")
        break 
    click_field[pos_y][pos_x] = 1
    horizontal_pattern = "---*"
    vertical_pattern = " |"
    line = "*" + horizontal_pattern*width
    for i in range(height):
        print(line)
        print("|", end = "")
        for j in range(width): 
            if click_field[i][j] == 0:
                print("  " + vertical_pattern, end = "")
            else: 
                print(" ", field[i][j], vertical_pattern, sep = "", end = "")
        #print("|" + vertical_pattern*width)
        print()
    print(line)
    

# set flags where are bombs 
# conditions of winning 
