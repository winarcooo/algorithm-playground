def reverse_string(num):
    str_num = str(num)

    rev_num = []
    for i in range(len(str_num), 0, -1):
        rev_num.append(str_num[i-1])

    if rev_num[0] == '0':
        rev_num.pop(0)
    
    if rev_num[len(rev_num)-1] == '-':
        rev_num.insert(0, rev_num.pop())
    
    return int(''.join(rev_num))


input = -120
print(reverse_string(input))