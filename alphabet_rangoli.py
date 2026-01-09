def print_rangoli(size):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    sliced_string = alphabet[:size]
    reverse_sliced = sliced_string[::-1]
    alphabet_rangoli_list = []
    len_max = 4*size - 3
    for item in range(size):
        first_half = reverse_sliced[:size-item]
        second_half = sliced_string[item+1:]
        full_string = first_half + second_half
        full_string = '-'.join(full_string)
        full_string = full_string.center(len_max,'-')
        alphabet_rangoli_list.append(full_string)

    final_list = alphabet_rangoli_list[:0:-1] + alphabet_rangoli_list
    for item in final_list:
        print(item)    

n = int(input())
print_rangoli(n)