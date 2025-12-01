cards = "23456789TJQKA"

def parse(input_file:str="camel_cards.in") -> list:
    with open(input_file) as f:
        return [line.strip().split(' ') for line in f.readlines()]

def fiveOfAKind(hand:str) -> bool:
    return len(set(hand)) == 1

def fourOfAKind(hand:str) -> bool:
    for card in cards:
        if hand.count(card) == 4:
            return True
    return False

def threeOfAKind(hand:str) -> bool:
    for card in cards:
        if hand.count(card) == 3:
            return True
    return False

def twoPair(hand:str) -> bool:
    pairs = 0
    for card in cards:
        if hand.count(card) == 2:
            pairs += 1
    return pairs == 2

def onePair(hand:str) -> bool:
    for card in cards:
        if hand.count(card) == 2:
            return True
    return False

def fullHouse(hand:str) -> bool:
    return threeOfAKind(hand) and onePair(hand)

def highCard(hand:str) -> bool:
    if len(set(hand)) == 5:
        return True
    return True

def evaluate(hand:str) -> tuple:
    numeric_value, pos = 0, 0
    for card in hand:
        numeric_value += (cards.index(card)+1) * (len(cards) ** (len(hand) - pos))
        pos += 1
    if fiveOfAKind(hand):
        return (7, numeric_value)
    elif fourOfAKind(hand):
        return (6, numeric_value)
    elif fullHouse(hand):
        return (5, numeric_value)
    elif threeOfAKind(hand):
        return (4, numeric_value)
    elif twoPair(hand):
        return (3, numeric_value)
    elif onePair(hand):
        return (2, numeric_value)
    elif highCard(hand):
        return (1, numeric_value)
    else:
        raise ValueError("That's not supposed to happen...")

def rankGame(game:list) -> list:
    return sorted(game, key=lambda x: evaluate(x[0]))

def scoreGame(game:list) -> int:
    total = 0
    ranked_game = rankGame(game)
    for i in range(len(ranked_game)):
        total += (i + 1) * int(ranked_game[i][1])
    return total

if __name__ == "__main__":
    game = parse()
    print(scoreGame(game))