def is_palindrome(s):
    l=0
    r=len(s)-1
    while l<=r:
        if s[l] != s[r]:
            return False
        l=l+1
        r=r-1
    return True

# a='Шалаш'
# print(is_palindrome(a))

b='Адрес'
print(is_palindrome(b))