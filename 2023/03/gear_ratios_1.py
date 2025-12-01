import re
with open('gear_ratios.in', 'r') as f:
    data = f.readlines()

issymbol = lambda x: x in '@#$%&+-=/*'
symbol_pos = list()
number_pos = dict()
numbers = list()
adjacent_numbers = list()

def isadjacent(pos1, symbol_pos, number_length):
    for pos2 in symbol_pos:
        for i in range(number_length):
            if abs(pos1[0]-pos2[0]) <= 1 and abs(pos1[1]+i-pos2[1]) <= 1:
                return True
    return False

for i in range(len(data)):
    numbers = re.findall(r"(\d+)", data[i])
    last = 0
    for k in range(len(numbers)):
        last += data[i][last:].index(numbers[k])
        number_pos[(i, last)] = int(numbers[k])
        last += len(numbers[k])
    for j in range(len(data[i])):
        if issymbol(data[i][j]):
            symbol_pos.append((i, j))

positions = number_pos.keys()
for pos in positions:
    value = number_pos[pos]
    if isadjacent(pos, symbol_pos, len(str(value))):
        adjacent_numbers.append(value)

print(sum(adjacent_numbers))
