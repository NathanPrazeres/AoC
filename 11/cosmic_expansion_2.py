def parse(input_file:str="test.in") -> list:
    with open(input_file, 'r') as f:
        lines = f.read().splitlines()
    empty_rows = []
    empty_cols = []
    for i in range(len(lines)):
        if all(x == "." for x in lines[i]):
            empty_rows.append(i)
    for i in range(len(lines[0])):
        if all(x == "." for x in [lines[j][i] for j in range(len(lines))]):
            empty_cols.append(i)
    galaxies = []
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            x = i
            y = j
            if lines[i][j] == "#":
                for row in empty_rows:
                    if i > row:
                        x += 999999
                for col in empty_cols:
                    if j > col:
                        y += 999999
                galaxies.append((x, y))
    return galaxies

# '....#........',
# '.........#...',
# '#............',
# '.............',
# '.............',
# '........#....',
# '.#...........',
# '............#',
# '.............',
# '.............',
# '.........#...',
# '#....#.......'


def distance(galaxy1:tuple, galaxy2:tuple) -> float:
    return abs(galaxy1[0] - galaxy2[0]) + abs(galaxy1[1] - galaxy2[1])

def totalDistance(galaxies:list) -> float:
    total = 0
    for i in range(len(galaxies)):
        for j in range(i + 1, len(galaxies)):
            total += distance(galaxies[i], galaxies[j])
    return total

if __name__ == "__main__":
    galaxies = parse("cosmic_expansion.in")
    print(totalDistance(galaxies))
