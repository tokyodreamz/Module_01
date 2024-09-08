from random import choice

employees = [
{"name": "Valera", "Position": "Manager", "department": "Sales"},
{"name": "Oleg", "Position": "Manager", "department": "Sales"},
{"name": "Oleg", "Position": "Developer", "department": "IT"},
{"name": "Olga", "Position": "Developer", "department": "IT"},
{"name": "Vladislav", "Position": "Manager", "department": "Sales"},
{"name": "Vladimir", "Position": "Developer", "department": "IT"},
{"name": "Anna", "Position": "Accountant", "department": "Finance"},
{"name": "Nastya", "Position": "Accountant", "department": "Finance"}
]
# def (Функция) - это обособленный контейнер, который будет обрабатывать какую либо задачу и будет выводить результат.
def find_name(name):
    '''Function find by name of employee and back to console'''
    for emp in employees: # Проходим по каждому сотруднику
      if emp["name"].lower() == name.lower():
          return emp

def count_employees(departament):
    '''Counting the number of employees'''
    count = 0
    for emp in employees: # Проходим по каждому сотруднику
       if emp["department"].lower() == departament.lower():
           count += 1
    return count # Возвращаем количество сотрудников

def add_emp(name, position, department):
    '''Add employee to the list'''
    for emp in employees:
        if emp["name"].lower() == name.lower():
            print(f"Employee with name {name} already exists.")
            return None
    new_employee = {
        "name": name,
        "Position": position,
        "department": department
    }
    employees.append(new_employee)
    return new_employee

while True:
    print('menu')
    print('1. Search employees')
    print('2. Counting the number of employees in department')
    print('3. Add employees')
    print('4. Exit the program')
    choice = input("Input number of menu: ")

    if choice == '1':
        name = input('Input target name: ')
        employee = find_name(name)
        if employee:
            print(f'\nEmployee find: {employee["name"]}'
                  f'\nPosition: {employee["Position"]}'
                  f'\nDepartment: {employee["department"]}')
        else:
            print('employee not found in company')

    elif choice == '2':
        department = input('Enter department')
        count_emp = count_employees(department)
        if count_emp: # Если сотрудники найдены
            print(f'\nCount {count_emp} in department {department}\n ')


    elif choice == '3':

        name = input('Enter name: ')

        position = input('Enter position: ')

        department = input('Enter department: ')

        new_emp = add_emp(name, position, department)

        if new_emp:
            print(f"Added new employee: {new_emp}")

    elif choice == '4':
      print('Goodbye!')
      break

    else:
        print(f'\nEnter the true\n')


