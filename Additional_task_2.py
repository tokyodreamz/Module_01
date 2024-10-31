import random
result = []
n = random.randint(3, 20)

for i in range(1, 21):
    for j in range(i, 21):

        if n % (i + j) == 0 and i != j:
            result.append(i)
            result.append(j)
print(*result, sep='')