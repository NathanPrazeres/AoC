def parse(input_file:str="mirage_maintenance.in"):
    with open(input_file, "r") as f:
        lines = f.read().splitlines()
    return [[int(x) for x in line.split()] for line in lines]

def calculatePrediction(history:list):
    diffs = [[] for _ in range(len(history))]
    current_line = history
    for i in range(len(current_line)):
        for j in range(1, len(current_line)):
            diffs[i].append(current_line[j] - current_line[j-1])
        current_line = diffs[i]
        if all([x == 0 for x in current_line]):
            current_line.insert(0, 0)
            break
    diffs.reverse()
    for i in range(0, len(diffs)-1):
        if diffs[i] == []:
            continue
        diffs[i+1].insert(0, diffs[i+1][0] - diffs[i][0])
    return history[0] - diffs[-1][0]

def solve(history_list:list):
    return sum([calculatePrediction(history) for history in history_list])

if __name__ == "__main__":
    history_list = parse()
    print(solve(history_list))