if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    newlist = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1)]
    newlist = [i for i in newlist if sum(i) != n]
    print(newlist)
