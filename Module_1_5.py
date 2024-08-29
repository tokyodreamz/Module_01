from xml.dom.minidom import ProcessingInstruction

immutable_var = ("Boom", 1, 3.14, True)
print(immutable_var)

try:
 immutable_var[1] = "World"
except TypeError as e:print("Ошибка при попытке изменить элемент кортежа:", e)
print("Кортежи являются неизменяемыми объектами. Это означает, что после создания кортежа его элементы нельзя изменить.")
mutable_list = ["Boom", 1, 3.14, True]
mutable_list[1] = "No War"
mutable_list.append(134)
print(mutable_list)