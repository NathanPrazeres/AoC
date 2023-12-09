def parse(input_file:str="haunted_wasteland.in"):
    with open(input_file, 'r') as f:
        data = f.read().splitlines()
    nav_instr = data[0]
    node_map = dict()
    for line in data[2:]:
        # Please ignore how awful this is:
        node_map[line.split()[0]] = (line.split("(")[1].split(",")[0], line.split("(")[1].split(",")[1][1:-1])
    return nav_instr, node_map

def lcm(node_list:list):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    lcm = node_list[0]
    for i in node_list[1:]:
        lcm = lcm*i//gcd(lcm, i)
    return lcm

def isEnding(node:str):
    return node[-1] == 'Z'

def traverseNodeMap(nav_instr:str, node_map:dict):
    steps = 0
    current_nodes = list()
    for node in node_map.keys():
        if node[-1] == 'A':
            current_nodes.append(node)
    node_endings = [-1 for _ in range(len(current_nodes))]
    while current_nodes:
        if -1 not in node_endings:
            break
        if nav_instr[steps%len(nav_instr)] == 'L':
            for i in range(len(current_nodes)):
                current_nodes[i] = node_map[current_nodes[i]][0]
        elif nav_instr[steps%len(nav_instr)] == 'R':
            for i in range(len(current_nodes)):
                current_nodes[i] = node_map[current_nodes[i]][1]
        steps += 1
        for i in range(len(current_nodes)):
            if node_endings[i] == -1 and isEnding(current_nodes[i]):
                node_endings[i] = steps
    return lcm(node_endings)

if __name__ == "__main__":
    nav_instr, node_map = parse()
    print(traverseNodeMap(nav_instr, node_map))