#!/usr/bin/env python3
arr = [2, 8, 9, 48, 8, 22, -12, 2]
new_arr = []
i = 0
while (i < len(arr)):
    if (arr[i] > 5):
        new_arr.append(arr[i] + 2)
    i = i + 1
print(arr)
print(new_arr)
