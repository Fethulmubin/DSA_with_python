def split_and_join(line):
    # write your code here
    splittedArr = line.split(" ")
    joinedString = "-".join(splittedArr)
    return joinedString
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
