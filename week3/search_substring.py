def search_substring(big_s, small_s):
    big_pointer=0
    small_pointer=0

    while big_pointer<=len(big_s)-1:
        if big_s[big_pointer]==small_s[small_pointer]:
            small_pointer=small_pointer+1
        elif small_pointer==big_pointer:
            small_pointer=0

        if small_pointer==len(small_s):
            return True
        big_pointer = big_pointer+1

    return False


# a='vvaaavv'
# b='aaa'
# print(search_substring(a,b))

a='ve5raabcabacbabasjfdkjdf'
b='vera'
print(search_substring(a,b))


