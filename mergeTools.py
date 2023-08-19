def merge_the_tools(string, k):
    # your code goes here
    chunks, chunk_size = len(string), k
    string_chunk = [string[i:i+chunk_size]
                    for i in range(0, chunks, chunk_size)]

    for i in string_chunk:
        res_list = []
        for item in i:
            if item not in res_list:
                res_list.append(item)

        print(''.join(res_list))
        
