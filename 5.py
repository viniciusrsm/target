def inv_str(str):
    str_list = []
    rev_str = []
    for i in range(len(str)):
        str_list.append(str[i])
    for i in range(len(str)):
        rev_str.append(str_list.pop())
    return "".join(rev_str)

print(inv_str("abcdef"))