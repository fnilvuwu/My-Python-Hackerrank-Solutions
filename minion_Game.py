def minion_game(string):
    # your code goes here
    score = {"Stuart": 0, "Kevin": 0}
    length = len(string)

    for i in range(length):
        if string[i] not in ('A', 'E', 'I', 'O', 'U'):
            score["Stuart"] += length - i
        else:
            score["Kevin"] += length - i

    if score["Kevin"] == score["Stuart"]:
        print("Draw")
    else:
        winner = max(score, key=score.get)
        print(winner, score[winner])

