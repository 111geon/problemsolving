import string

strings = input().upper()

d = {}
for l in string.ascii_uppercase:
    d[l] = 0

for s in strings:
    d[s] += 1

max_val = max(d.values())
max_keys = []
for k, v in d.items():
    if v == max_val:
        max_keys.append(k)

if len(max_keys) > 1:
    print('?')

else:
    print(max_keys[0])
