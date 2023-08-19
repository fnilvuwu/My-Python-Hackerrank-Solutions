from collections import OrderedDict
ordered_dictionary = OrderedDict()
N = int(input())
for i in range(N):
    string_list = input().split()
    product = ' '.join(string_list[:len(string_list)-1])
    price = int(string_list[len(string_list) - 1])

    if product in ordered_dictionary:
        ordered_dictionary[product] = ordered_dictionary[product] + price
    else:
        ordered_dictionary[product] = price

for item in ordered_dictionary:
    print(item + " " + str(ordered_dictionary[item]))
