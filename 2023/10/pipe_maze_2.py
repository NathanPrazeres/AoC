def parse_file(input_file:str="test.in") -> dict:
    with open(input_file) as f:
        temp = [line.rstrip('\n') for line in f]
    maze = dict()
    for i in range(len(temp)):
        for j in range(len(temp[i])):
            if temp[i][j] == 'S':
                maze["Start"] = (i, j)
            else:
                maze[(i, j)] = temp[i][j]
    return maze

def mazePath(maze:dict) -> dict:
    start_position = maze["Start"]
    startType(maze)
    path = dict()
    path[start_position] = maze[start_position]
    queue = [start_position]
    while queue:
        current_position = queue.pop(0)
        for position in adjacentPositions(current_position, maze[current_position]):
            if position not in path:
                path[position] = maze[position]
                queue.append(position)
    for x in range(max(path, key=lambda x: x[0])[0] + 1):
        for y in range(max(path, key=lambda x: x[1])[1] + 1):
            if (x, y) not in path:
                path[(x, y)] = '.'
    return path

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

def outOfBounds(position:tuple, maze:dict) -> bool:
    x, y = position
    for key in maze.keys():
        if key == "Start":
            continue
        max_x = max(key[0], x)
        max_y = max(key[1], y)
    return x < 0 or y < 0 or x >= max_x or y >= max_y

def startType(maze:dict) -> str:
    start_position = maze["Start"]
    for type in ['L', 'F', 'J', '7', '-', '|']:
        correct = True
        adjacent = adjacentPositions(start_position, type)
        for position in adjacent:
            if outOfBounds(position, maze) or start_position not in adjacentPositions(position, maze[position]):
                correct = False
                break
        if correct:
            maze[start_position] = type
            return type

def interiorPoints(maze:dict) -> int:
    total = 0
    path = [(x, y) for x, y in maze.keys() if maze[(x, y)] != '.']
    spaces = [(x, y) for x, y in maze.keys() if maze[(x, y)] == '.']
    max_x = max(path, key=lambda x: x[0])[0]
    max_y = max(path, key=lambda x: x[1])[1]
    for space in spaces:
        if space[0] == 0 or space[0] == max_x or space[1] == 0 or space[1] == max_y:
            continue
        intersections1, intersections2, intersections3, intersections4 = 0, 0, 0, 0
        last = "."
        for x in range(0, space[0]):
            if maze[(x, space[1])] == '|':
                continue
            if (x, space[1]) in path:
                if maze[(x, space[1])] == '-':
                    intersections1 += 1
                    last = "."
                elif maze[(x, space[1])] in ['L', 'F']:
                    if last in "J7":
                        last = "."
                        continue
                    else:
                        intersections1 += 1
                        if last in "LF":
                            last = "."
                        else:
                            last = maze[(x, space[1])]
                elif maze[(x, space[1])] in ['J', '7']:
                    if last in "LF":
                        last = "."
                        continue
                    else:
                        intersections1 += 1
                        if last in "J7":
                            last = "."
                        else:
                            last = maze[(x, space[1])]
        if intersections1 % 2 == 0:
            continue
        last = "."
        for x in range(space[0] + 1, max_x + 1):
            if maze[(x, space[1])] == '|':
                continue
            if (x, space[1]) in path:
                if maze[(x, space[1])] == '-':
                    intersections2 += 1
                    last = "."
                elif maze[(x, space[1])] in ['L', 'F']:
                    if last in "J7":
                        last = "."
                        continue
                    else:
                        intersections2 += 1
                        if last in "LF":
                            last = "."
                        else:
                            last = maze[(x, space[1])]
                elif maze[(x, space[1])] in ['J', '7']:
                    if last in "LF":
                        last = "."
                        continue
                    else:
                        intersections2 += 1
                        if last in "J7":
                            last = "."
                        else:
                            last = maze[(x, space[1])]
        if intersections2 % 2 == 0:
            continue
        last = "."
        for y in range(0, space[1]):
            if maze[(space[0], y)] == '-':
                continue
            if (space[0], y) in path:
                if maze[(space[0], y)] == '|':
                    intersections3 += 1
                    last = "."
                elif maze[(space[0], y)] in ['J', 'L']:
                    if last in "F7":
                        last = "."
                        continue
                    else:
                        intersections3 += 1
                        if last in "JL":
                            last = "."
                        else:
                            last = maze[(space[0], y)]
                elif maze[(space[0], y)] in ['F', '7']:
                    if last in "JL":
                        last = "."
                        continue
                    else:
                        intersections3 += 1
                        if last in "F7":
                            last = "."
                        else:
                            last = maze[(space[0], y)]
        if intersections3 % 2 == 0:
            continue
        last = "."
        for y in range(space[1] + 1, max_y + 1):
            if maze[(space[0], y)] == '-':
                continue
            if (space[0], y) in path:
                if maze[(space[0], y)] == '|':
                    intersections4 += 1
                    last = "."
                elif maze[(space[0], y)] in ['J', 'L']:
                    if last in "F7":
                        last = "."
                        continue
                    else:
                        intersections4 += 1
                        if last in "JL":
                            last = "."
                        else:
                            last = maze[(space[0], y)]
                elif maze[(space[0], y)] in ['F', '7']:
                    if last in "JL":
                        last = "."
                        continue
                    else:
                        intersections4 += 1
                        if last in "F7":
                            last = "."
                        else:
                            last = maze[(space[0], y)]
        if intersections4 % 2 == 0:
            continue
        total += 1
    return total

def printMaze(maze:dict) -> None:
    max_x = max(maze, key=lambda x: x[0])[0]
    max_y = max(maze, key=lambda x: x[1])[1]
    for x in range(max_x + 1):
        for y in range(max_y + 1):
            if (x, y) in maze:
                print(maze[(x, y)], end="")
            else:
                print(".", end="")
        print()

if __name__ == "__main__":
    maze = mazePath(parse_file("pipe_maze.in"))
    # printMaze(maze)
    print(interiorPoints(maze))