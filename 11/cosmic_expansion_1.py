def parse(input_file:str="test.in") -> list:
    with open(input_file, 'r') as f:
        lines = f.read().splitlines()
    lines1 = lines.copy()
    blank_lines = 0
    for i in range(len(lines)):
        if all(x == "." for x in lines[i]):
            lines1.insert(i + blank_lines, "." * len(lines[i]))
            blank_lines += 1
    lines2 = lines1.copy()
    blank_lines = 0
    for i in range(len(lines1[0])):
        if all(x == "." for x in [lines1[j][i] for j in range(len(lines1))]):
            for j in range(len(lines1)):
                lines2[j] = lines2[j][:i + blank_lines] + "." + lines2[j][i + blank_lines:]
            blank_lines += 1
    galaxies = []
    for i in range(len(lines2)):
        for j in range(len(lines2[i])):
            if lines2[i][j] == "#":
                galaxies.append((i, j))
    return galaxies

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
