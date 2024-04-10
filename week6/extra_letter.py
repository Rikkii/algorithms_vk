def extra_letter(a,b):
    hash_map_a = dict()

    for i in range(len(a)):
        hash_map_a[a[i]] += 1

    for i in range(len(b)):
        if b[i] in hash_map_a:
            hash_map_a[b[i]] -= 1
            if hash_map_a[b[i]] == 0:
                hash_map_a.pop(b[i])

            continue
        return b[i]
    return ""

a = 'sun'
b='enus'

print(extra_letter(a,b))