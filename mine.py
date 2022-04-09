import random
field = []
width = 10 
height = 10 
bomb_numbers = 5
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


    
    
# create a field with 0
# add bombs to the field 
# create a table instead of list
# add numbers to the field 
# conditions for gameplay 