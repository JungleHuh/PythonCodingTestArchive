n = int(input())

array = []
for _ in range(n):
    array.append(input())

    array = sorted(array, reverse = True)

for i in array:
    print(i, end = " ")