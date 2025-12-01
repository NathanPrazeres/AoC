def parse_file(input_file:str="test.in") -> dict:
    with open(input_file) as f:
        temp = [line.rstrip('\n') for line in f]
    maze = dict()
    for i in range(len(temp)):
        for j in range(len(temp[i])):
            if temp[i][j] == 'S':
                maze["Start"] = (i, j)
            elif temp[i][j] != '.':
                maze[(i, j)] = temp[i][j]
    return maze

def adjacentPositions(position:tuple, type:str) -> list:
    x, y = position
    if type == 'L':
        return [(x-1, y), (x, y+1)]
    elif type == 'F':
        return [(x+1, y), (x, y+1)]
    elif type == 'J':
        return [(x, y-1), (x-1, y)]
    elif type == '7':
        return [(x, y-1), (x+1, y)]
    elif type == '-':
        return [(x, y-1), (x, y+1)]
    elif type == '|':
        return [(x-1, y), (x+1, y)]
    else:
        return []

def startType(maze:dict) -> str:
    start_position = maze["Start"]
    for type in ['L', 'F', 'J', '7', '-', '|']:
        correct = True
        adjacent = adjacentPositions(start_position, type)
        for position in adjacent:
            if start_position not in adjacentPositions(position, maze[position]):
                correct = False
        if correct:
            maze[start_position] = type
            return type

def distances(maze:dict) -> dict:
    start_position = maze["Start"]
    startType(maze)
    distances = dict()
    distances[start_position] = 0
    queue = [start_position]
    while queue:
        current_position = queue.pop(0)
        for position in adjacentPositions(current_position, maze[current_position]):
            if position not in distances or distances[position] > distances[current_position] + 1:
                distances[position] = distances[current_position] + 1
                queue.append(position)
    return distances

def farthestPipe(maze:dict) -> tuple:
    d = distances(maze)
    return d[max(d, key=d.get)]

if __name__ == "__main__":
    maze = parse_file("pipe_maze.in")
    print(farthestPipe(maze))