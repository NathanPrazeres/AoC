import re
with open('test.in', 'r') as f:
    data = f.readlines()

isgear = lambda x: x == '*'
gear_pos = dict()
number_pos = dict()
total = 0

for i in range(len(data)):
    numbers = re.findall(r"(\d+)", data[i])
    last = 0
    for k in range(len(numbers)):
        last += data[i][last:].index(numbers[k])
        number_pos[(i, last)] = int(numbers[k])
        last += len(numbers[k])
    for j in range(len(data[i])):
        if isgear(data[i][j]):
            gear_pos[(i, j)] = data[i][j]

for (pos_x, pos_y), value in gear_pos.items():
    if value == '*':
        temp_number_pos = []
        for pos in number_pos.keys():
            for i in range(len(str(number_pos[pos]))):
                if abs(pos[0]-pos_x) <= 1 and abs(pos[1]-pos_y+i) <= 1:
                    temp_number_pos.append(pos)
                    break
        if len(temp_number_pos) == 2:
            print(temp_number_pos)
            total += number_pos[temp_number_pos[0]] * number_pos[temp_number_pos[1]]

print(total)
