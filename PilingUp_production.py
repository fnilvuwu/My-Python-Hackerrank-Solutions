# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(input())
output = []
for i in range(T):
    input()
    blocks = [int(i) for i in input().split()]

    left_block = blocks[0:blocks.index(min(blocks))]
    right_block = blocks[blocks.index(min(blocks)):len(blocks)]
    stackable = []

    if sorted(left_block) == left_block or sorted(left_block) == left_block[::-1]:
        stackable.append(True)
        # print("left block is sorted")
    else:
        stackable.append(False)

    if sorted(right_block) == right_block or sorted(right_block) == right_block[::-1]:
        stackable.append(True)
        # print("right block is sorted")
    else:
        stackable.append(False)

    if all(stackable):
        output.append("Yes")
        # print("Yes")
    else:
        output.append("No")
        # print("No")

for i in output:
    print(i)
