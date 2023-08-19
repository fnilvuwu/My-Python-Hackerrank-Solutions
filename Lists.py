if __name__ == '__main__':
    N = int(input())
    array_list = []
    for i in range(N):
        x = input()
        command = x.split(" ")[0]
        if (command == "append"):
            _, num = x.split(" ")
            array_list.append(int(num))
        elif (command == "remove"):
            _, num = x.split(" ")
            array_list.remove(int(num))
        elif (command == "insert"):
            _, num, index = x.split(" ")
            array_list.insert(int(num), int(index))
        elif (command == "print"):
            print(array_list)
        elif (command == "sort"):
            array_list.sort()
        elif (command == "pop"):
            array_list.pop()
        elif (command == "reverse"):
            array_list.reverse()
