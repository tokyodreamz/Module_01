first = int(input("Введите первое число: "))
second = int(input("Введите первое число: "))
third = int(input("Введите первое число: "))
if first == second == third:
    print(3,'Числа равны')
elif first == second or first == third or second == third:
    print(2,'Числа равны')
else:
    print(0,'Совпадений нет')