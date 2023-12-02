sum = 0
n = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
     "six": 6, "seven": 7, "eight": 8, "nine": 9}

def isdigit(c):
    return c >= '0' and c <= '9'

def isnumber(c):
    for i in range(len(c)):
        if c[0:i] in n:
            return i
    return -1

if __name__ == "__main__":
    with open("trebuchet.in", "r") as input_file:
        for line in input_file:
            numbers = []
            for i in range(len(line)):
                if isdigit(line[i]):
                    numbers.append(int(line[i]))
                    continue
                length = isnumber(line[i:])
                if length > 0:
                    numbers.append(n[line[i:length + i]])
            sum += numbers[0] * 10 + numbers[-1]
    print(sum)