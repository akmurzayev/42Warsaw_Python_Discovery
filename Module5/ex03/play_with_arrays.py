#!/usr/bin/env python3
arr = [2, 8, 9, 48, 8, 22, -12, 2]
uniq_arr = set(arr)
new_arr = set()
x = 0
for x in uniq_arr:
    if x > 5:
        new_arr.add(x + 2)
print(new_arr)

