def generate_password(n):
    result = ""
    for i in range(1, 21):
        for j in range(i + 1, 21):
            if (i + j) % n == 0:
                result += str(i) + str(j)
    return result

result1 = generate_password(9)
result2 = generate_password(11)
result3 = generate_password(18)

print(result1)
print(result2)
print(result3)