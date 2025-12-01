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

def lowestSeedLocation(m:dict) -> dict:
    seedGroups = []
    for i in range(0, len(m['seeds']), 2):
        seedGroups.append([m['seeds'][i], m['seeds'][i] + m['seeds'][i+1]])
    for type, translationList in m.items():
        newSeedGroups = []
        if type == 'seeds':
            continue
        for begin, end in seedGroups:
            for translation in translationList:
                dest = translation[0]
                src = translation[1]
                r = translation[2]
                overlaping = [max(begin, src), min(end, src + r)]
                if overlaping[0] < overlaping[1]:
                    newSeedGroups.append([overlaping[0] - src + dest, overlaping[1] - src + dest])
                    if overlaping[0] > begin:
                        seedGroups.append([begin, overlaping[0]])
                    if overlaping[1] < end:
                        seedGroups.append([overlaping[1], end])
                    break
            else:
                newSeedGroups.append([begin, end])
        seedGroups = newSeedGroups
        print(seedGroups)
    print(seedGroups)
    return min(seedGroups)[0] # Lower bound of the lowest seed group



if __name__ == "__main__":
    m = processInputFile()
    lowestLocation = lowestSeedLocation(m)
    print(lowestLocation)