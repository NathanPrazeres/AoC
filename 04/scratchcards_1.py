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
    points = 0
    for card in cardList:
        numbers = card[0]
        yourNumbers = card[1]
        n = winningNumbers(numbers, yourNumbers)
        if len(n) > 0:
            points += 2**(len(n)-1)
    return points

if __name__ == '__main__':
    cardList = readInput("scratchcards.in")
    print(calculatePoints(cardList))