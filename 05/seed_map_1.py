def processInputFile(filename:str='seed_map.in') -> dict:
    with open(filename, 'r') as f:
        lines = f.readlines()
    m = dict()
    m['seeds'] = [int(x) for x in lines[0].split(" ")[1:]]
    m['seed-soil'], m['soil-fert'], m['fert-water'], m['water-light'], m['light-temp'], m['temp-hum'], m['hum-loc'] = [], [], [], [], [], [], []
    type = 1
    flag = False
    for line in lines[3:]:
        if line == "\n":
            type += 1
            flag = True
            continue
        if flag: # Skip the header line of each type
            flag = False
            continue
        if type == 1:
            m['seed-soil'].append([int(x) for x in line.split("\n")[0].split(" ")])
        elif type == 2:
            m['soil-fert'].append([int(x) for x in line.split("\n")[0].split(" ")])
        elif type == 3:
            m['fert-water'].append([int(x) for x in line.split("\n")[0].split(" ")])
        elif type == 4:
            m['water-light'].append([int(x) for x in line.split("\n")[0].split(" ")])
        elif type == 5:
            m['light-temp'].append([int(x) for x in line.split("\n")[0].split(" ")])
        elif type == 6:
            m['temp-hum'].append([int(x) for x in line.split("\n")[0].split(" ")])
        elif type == 7:
            m['hum-loc'].append([int(x) for x in line.split("\n")[0].split(" ")])
    return m

def getSeedMap(m:dict) -> dict:
    seedMap = dict()
    for i in range(len(m['seeds'])):
        seed = m['seeds'][i]
        for type, translationList in m.items():
            if type == 'seeds':
                continue
            transaltionExists = False
            for translation in translationList:
                dest = translation[0]
                src = translation[1]
                r = translation[2] - 1
                if seed >= src and seed <= src + r:
                    seed = dest + seed - src
                    transaltionExists = True
                    break
            if not transaltionExists:
                continue
        seedMap[m['seeds'][i]] = seed
    return seedMap

def lowestLocation(seedMap:dict) -> int:
    first = True
    for _, location in seedMap.items():
        if first:
            lowest = location
            first = False
            continue
        if location < lowest:
            lowest = location
    return lowest

if __name__ == "__main__":
    m = processInputFile()
    seedMap = getSeedMap(m)
    lowest = lowestLocation(seedMap)
    print(lowest)