from pprint import PrettyPrinter

my_dict = {'David':1990, 'Mary':1988, 'John':2001}
print(my_dict)
print("Год рождения David:", my_dict["David"])
print("Год рождения Alice:", my_dict.get("Alice", "Значение не найдено"))
my_dict.update({'Frank':1566,
                'Bertram':1891})
print(my_dict)
removed_value = my_dict.pop(""'Frank', "Значение не найдено")
print("Удаленное значение для ключа 'Frank':", removed_value)
print(my_dict)
my_set = {1,1,2,2,'David','Bertram'}
print("Множество my_set:", my_set)
my_set.add("Bob")
my_set.add(5)
print("Множество my_set после добавления новых элементов:", my_set)
my_set.remove(2)
print("Множество my_set после удаления элемента:", my_set)