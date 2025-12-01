n = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
     "six": 6, "seven": 7, "eight": 8, "nine": 9}

def isnumber(c):
    for i in range(len(c)):
        if c[0:i] in n:
            return i
    return -1

if __name__ == "__main__":
    sum = 0
    with open("trebuchet.in", "r") as input_file:
        for line in input_file:
            numbers = []
            for i in range(len(line)):
                if line[i].isdigit():
                    numbers.append(int(line[i]))
                    continue
                length = isnumber(line[i:])
                if length > 0:
                    numbers.append(n[line[i:length + i]])
            sum += numbers[0] * 10 + numbers[-1]
    print(sum)