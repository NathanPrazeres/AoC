if __name__ == "__main__":
    sum = 0
    with open("trebuchet.in", "r") as input_file:
        for line in input_file:
            first, last = 0, 0
            first_flag, last_flag = False, False
            for i in range(len(line)):
                if not first_flag and line[i].isdigit():
                    first = int(line[i])
                    first_flag = True
                if not last_flag and line[len(line) - i - 1].isdigit():
                    last = int(line[len(line) - i - 1])
                    last_flag = True
                if first_flag and last_flag:
                    break
            sum += first * 10 + last
    print(sum)