a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 1]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

result = []
for elem in a:
    if elem in b:
        result.append(elem)

print(result)
