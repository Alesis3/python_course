
width, height = [int(i) for i in input().split()]
amount = int(input())
positions = []
for i in range(amount):
    inputs = input().split()
    s = inputs[0]
    position = int(inputs[1])
    positions.append((s, position))


for coordinate_y in range(height):
    print('|', end='')
    for coordinate_x in range(width):
        char = ' '

        for sand in positions:
            if sand[1] == coordinate_x:
                char = sand[0]


        print(char, end='')

    print('|')

print('+' + '-' * width + '+')