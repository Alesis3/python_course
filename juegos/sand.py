
width, height = [int(i) for i in input().split()]
amount = int(input())
positions = []

def is_empty(x, y):
    if x < 0 or x >= width or y < 0 or y >= height:
        return False
    for sand in positions:
        if sand[1] == x and sand[2] == y:
            return False
    return True


for _ in range(amount):
    s, col = input().split()
    col = int(col)
    coordinate_x, coordinate_y = col, -1

    while True:
        if is_empty(coordinate_x, coordinate_y + 1):
            coordinate_y += 1
            continue

        moved = False
        if s.islower():
            if is_empty(coordinate_x + 1, coordinate_y + 1):
                coordinate_x += 1
                coordinate_y += 1
                moved = True
            elif is_empty(coordinate_x - 1, coordinate_y + 1):
                coordinate_x -= 1
                coordinate_y += 1
                moved = True
        else:
            if is_empty(coordinate_x - 1, coordinate_y + 1):
                coordinate_x -= 1
                coordinate_y += 1
                moved = True
            elif is_empty(coordinate_x + 1, coordinate_y + 1):
                coordinate_x += 1
                coordinate_y += 1
                moved = True

        if not moved:
            positions.append([s, coordinate_x, coordinate_y])
            break

#creacion del tablero
for coordinate_y in range(height):
    print('|', end='')
    for coordinate_x in range(width):
        char = ' '

        for sand in positions:
            if sand[1] == coordinate_x and sand[2] == coordinate_y and char == ' ':
                char = sand[0]

        print(char, end='')

    print('|')

print('+' + '-' * width + '+')
