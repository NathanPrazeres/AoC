def parseFile(input_file:str="boat_races.in") -> list:
    with open(input_file, 'r') as file:
        data = [line.strip().split(':')[1].strip(' ').split(' ') for line in file.readlines()]
    data = [[int(''.join([x for x in line if x != '']))] for line in data]
    return data

def possibleTimes(time:int, distance:int) -> list:
    possible = []
    for t in range(1, time):
        if (time - t) * t > distance:
            possible.append(t)
    return possible

def solve(data:list) -> list:
    result = 1
    times = data[0]
    distances = data[1]
    for i in range(len(times)):
        result *= len(possibleTimes(times[i], distances[i]))
    return result

if __name__ == "__main__":
    data = parseFile()
    print(solve(data))