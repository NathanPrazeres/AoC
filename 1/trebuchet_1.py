input_file = open("trebuchet.in", "r")
sum = 0

def isdigit(c):
    return c >= '0' and c <= '9'

if __name__ == "__main__":
    for line in input_file:
        first, last = 0, 0
        first_flag, last_flag = False, False
        for i in range(len(line)):
            if not first_flag and isdigit(line[i]):
                first = int(line[i])
                first_flag = True
            if not last_flag and isdigit(line[len(line) - i - 1]):
                last = int(line[len(line) - i - 1])
                last_flag = True
            if first_flag and last_flag:
                break
        sum += first * 10 + last
    print(sum)