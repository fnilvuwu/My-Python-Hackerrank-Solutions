if __name__ == '__main__':
    records = []
    grade = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])
        grade.append(score)
        
    records = sorted(records)
    second_lowest = sorted(set(grade))[1]

    for i in records:
        if i[1] == second_lowest:
            print(i[0])
