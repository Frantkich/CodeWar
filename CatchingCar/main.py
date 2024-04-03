

def next_bigger(n):
    n_list = [int(x) for x in str(n)]
    n_list_len = len(n_list)
    if n_list_len == 1:
        return -1
    for offset in range(n_list_len-1):
        i = n_list_len - offset - 1
        if n_list[i-1] < n_list[i]:
            n_list_beg = n_list[:i]
            n_list_end = n_list[i:]
            for x in range(n_list[i-1]+1, 10):
                if x in n_list_end:
                    rotate_index = n_list_end.index(x)
                    break
            n_list_beg[i-1], n_list_end[rotate_index] = n_list_end[rotate_index], n_list_beg[i-1]
            n_list_end.sort()
            return int("".join([str(n) for n in n_list_beg + n_list_end]))
    return -1 

tests = [[  12,   21], [  21,   -1], [ 513,  531], [2017, 2071], [ 414,  441], [ 144,  414], [1234567890, 1234567908], [59884848459853, 59884848483559]]
for test in tests:
    result = next_bigger(test[0])
    if result != test[1]:
        print("---------")
        print(test[0])
        print(test[1])
        print(result)
        break
    # else:
    #     print(f"Okay: {test[0]}")