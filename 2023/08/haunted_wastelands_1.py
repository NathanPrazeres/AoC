def parse(input_file:str="haunted_wasteland.in"):
    with open(input_file, 'r') as f:
        data = f.read().splitlines()
    nav_instr = data[0]
    node_map = dict()
    for line in data[2:]:
        # Please ignore how awful this is:
        node_map[line.split()[0]] = (line.split("(")[1].split(",")[0], line.split("(")[1].split(",")[1][1:-1])
    return nav_instr, node_map

def traverseNodeMap(nav_instr:str, node_map:dict, start:str="AAA", end:str="ZZZ"):
    steps = 0
    current_node = start
    while True:
        if current_node == end:
            break
        if nav_instr[steps%len(nav_instr)] == 'L':
            current_node = node_map[current_node][0]
        elif nav_instr[steps%len(nav_instr)] == 'R':
            current_node = node_map[current_node][1]
        steps += 1
    return steps

if __name__ == "__main__":
    nav_instr, node_map = parse()
    print(traverseNodeMap(nav_instr, node_map))