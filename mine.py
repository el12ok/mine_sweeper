import random
field = []
width = 10 
height = 10 
bomb_numbers = 10
bomb_icon = 9
#pos_x = int(input())
#pos_y = int(input())
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

pprint(field)
    
    
# create a field with 0
# add bombs to the field 
# add numbers to the field 
# create a table instead of list
# conditions for gameplay 