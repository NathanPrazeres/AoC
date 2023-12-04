def readInput(file_name:str="test.in")->list:
    with open(file_name, "r") as f:
        lines = f.read().splitlines()
    newLines = []
    for line in lines:
        line = line.split(":")
        line = line[1].split("|")
        line = [[x for x in line[0].split(' ') if x != ''], [x for x in line[1].split(' ') if x != '']]
        newLines.append(line)
    return newLines

def winningNumbers(numbers:list, yourNumbers:list)->list:
    winningNumbers = []
    for number in yourNumbers:
        if number in numbers:
            winningNumbers.append(number)
    return winningNumbers

def calculatePoints(cardList:list)->int:
    points, repetitions = list(), list()
    for card in cardList:
        numbers = card[0]
        yourNumbers = card[1]
        n = winningNumbers(numbers, yourNumbers)
        points.append(len(n))
    for _ in points:
        repetitions.append(1)
    for i in range(len(points)):
        if points[i] == 0:
            continue
        else:
            for j in range(1, points[i]+1):
                if i+j >= len(points):
                    break
                repetitions[i+j] += repetitions[i]
    return sum(repetitions)

if __name__ == '__main__':
    cardList = readInput("scratchcards.in")
    print(calculatePoints(cardList))