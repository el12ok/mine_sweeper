from dis import code_info
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
        
type_click = ["open cell", "set a bomb", "remove a bomb"]
while True: 
    for index, value in enumerate(type_click): 
        print(index, value)
    print()
    action = int(input("Choose the number for action:")) 
    print()
    if action > 2 or action < 0: 
        print("Error. Incorrect number, try again")
        print()
        continue
    pos_x, pos_y = input(("Enter coordinates x&y: ")).split()
    pos_x = int(pos_x)-1
    pos_y = int(pos_y)-1
    if any((pos_x<0, pos_x >= width, pos_y < 0, pos_y >= height)):
        print("Error: out of range. Try again")
        print()
        continue

#game logic
    if action == 0: 
        if field[pos_y][pos_x] == bomb_icon:
            print("Game over")
            break 
        click_field[pos_y][pos_x] = 1
    elif action == 1 and click_field[pos_y][pos_x] == 0:
        click_field[pos_y][pos_x] = "B" 
    elif action == 2 and click_field[pos_y][pos_x] == "B": 
        click_field[pos_y][pos_x] = 0

    count_bomb = 0
    count_flag = 0
    for i in range(height): 
        for j in range(width): 
            if click_field[i][j] == "B": 
                count_flag += 1 
                if field[i][j] == bomb_icon: 
                    count_bomb += 1
    if count_bomb == count_flag and count_bomb == bomb_numbers: 
        print("Congratulations! You win!")
        break

    horizontal_pattern = "---*"
    vertical_pattern = " |"
    line = "*" + horizontal_pattern*width
    for i in range(height):
        print(line)
        print("|", end = "")
        for j in range(width): 
            if click_field[i][j] == 0:
                print("  " + vertical_pattern, end = "")
            elif click_field[i][j] == "B": 
                print(" B" + vertical_pattern, end = "")
            else: 
                print(" ", field[i][j], vertical_pattern, sep = "", end = "")
        #print("|" + vertical_pattern*width)
        print()
    print(line)
    
horizontal_pattern = "---*"
vertical_pattern = " |"
line = "*" + horizontal_pattern*width
for i in range(height):
    print(line)
    print("|", end = "")
    for j in range(width): 
        if field[i][j] == 0:
            print("  " + vertical_pattern, end = "")
        else: 
            print(" ", field[i][j], vertical_pattern, sep = "", end = "")
    #print("|" + vertical_pattern*width)
    print()
print(line)

# set flags where are bombs 
# conditions of winning 
