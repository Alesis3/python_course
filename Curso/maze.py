import os
import random
import readchar

obstacle_definition = """\
            ####         
#  #######           ####
##   ############    ####
## #####                 
##  #####  #######    ###
#  #########            #
#   ####          #######
##    #######         ###
####   ###    ###       #
#####                 ###
#########  #####         
######    ##########   ##
#######               ###\
"""

MY_POSX = 0
MY_POSY = 1
NUM_OBJECT_MAP = 10

tail = []
tail_length = 0
object = []
position = [0, 0]
died = False

obstacle_definition = [list(row) for row in obstacle_definition.split("\n")]

MAP_WIDTH = len(obstacle_definition[0])
MAP_HEIGHT = len(obstacle_definition)

while True:

    while len(object) < NUM_OBJECT_MAP:
        new_object = [random.randint(0, MAP_WIDTH), random.randint(0, MAP_HEIGHT)]

        if new_object not in object and new_object != position:
            object.append(new_object)

    print("+" + "-" * MAP_WIDTH * 3 + "+")

    for coordinate_y in range(MAP_HEIGHT):
        print("|", end="")
        for coordinate_x in range(MAP_WIDTH):

            char = " "
            object_delete = None
            tail_cell = None

            for object_s in object:
                if object_s[MY_POSX] == coordinate_x and object_s[MY_POSY] == coordinate_y:
                    char = "*"
                    object_delete = object_s

            for tail_piece in tail:
                if tail_piece[MY_POSX] == coordinate_x and tail_piece[MY_POSY] == coordinate_y:
                    char = "O"
                    tail_cell = tail_piece



            if obstacle_definition[coordinate_y][coordinate_x] == "#":
                char = "#"

            print(" {} ".format(char), end="")
        print("|")


    print("+" + "-" * MAP_WIDTH * 3 + "+")

    if position[MY_POSX] == coordinate_x and position[MY_POSY] == coordinate_y:
        char = "@"

        if object_delete:
            object.remove(object_delete)
            tail_length += 1

        if tail_cell:
            print("Has chocado")
            died = True

        if obstacle_definition[coordinate_y][coordinate_x] == "#":
            died = True

    if died == True:
        print("x" * MAP_WIDTH + "¡Perdiste!" + "x" * MAP_WIDTH)
        break

    direction = readchar.readchar()

    if direction == "w":
        tail.insert(0, position.copy())
        tail = tail[:tail_length]
        position[MY_POSY] -= 1
        position[MY_POSY] %= MAP_HEIGHT
    elif direction == "s":
        tail.insert(0, position.copy())
        tail = tail[:tail_length]
        position[MY_POSY] += 1
        position[MY_POSY] %= MAP_HEIGHT
    elif direction == "d":
        tail.insert(0, position.copy())
        tail = tail[:tail_length]
        position[MY_POSX] += 1
        position[MY_POSX] %= MAP_WIDTH
    elif direction == "a":
        tail.insert(0, position.copy())
        tail = tail[:tail_length]
        position[MY_POSX] -= 1
        position[MY_POSX] %= MAP_WIDTH
    elif direction == "b":
        break

    os.system("clear")
