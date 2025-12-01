red = 12
green = 13
blue = 14

sum = 0

with open('cube_conundrum.in', 'r') as f:
    data = f.readlines()

for l in data:
    flag = True
    line = l.replace(',', '').replace(';', '').replace(':', '').split()
    game_number = int(line[1])
    for i in range(2, len(line), 2):
        if line[i+1] == 'red' and int(line[i]) > red:
            flag = False
        elif line[i+1] == 'green' and int(line[i]) > green:
            flag = False
        elif line[i+1] == 'blue' and int(line[i]) > blue:
            flag = False
    if flag:
        sum += game_number
print(sum)