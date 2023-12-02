sum = 0

with open('cube_conundrum.in', 'r') as f:
    data = f.readlines()

for l in data:
    red, green, blue = 0, 0, 0
    line = l.replace(',', '').replace(';', '').replace(':', '').split()
    game_number = int(line[1])
    for i in range(2, len(line), 2):
        if line[i+1] == 'red' and int(line[i]) > red:
            red = int(line[i])
        elif line[i+1] == 'green' and int(line[i]) > green:
            green = int(line[i])
        elif line[i+1] == 'blue' and int(line[i]) > blue:
            blue = int(line[i])
    sum += (red * green * blue)
print(sum)