A = [1, 2, 3, 4]
B = [3, 4, 5, 6]

C = []

for i in A:
    if i not in C:
        C.append(i)

for i in B:
    if i not in C:
        C.append(i)

print(C)