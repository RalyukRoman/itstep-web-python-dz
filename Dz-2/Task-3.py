employees = {
    'Ivanov Ivan': {
        'phone': '+380501234567',
        'corporate email': 'ivanov@company.com',
        'job': 'Software Engineer',
        'office number': '404',
        'skype': 'live:ivanov_dev' 
    },
    'Petrenko Maria': {
        'phone': '+380679876543',
        'corporate email': 'petrenko@company.com',
        'job': 'Project Manager',
        'office number': '201',
        'skype': 'm.petrenko_hr' 
    }
}

def inputName():
    title = input('Enter full name: ')
    return title.strip().title()

def printEmployee(name):
    info = employees[name]
    print(f'\n{name}: ')
    for key, value in info.items():
        print(f'  {key} = {value}')

def printAllEmployees():
    print('\n', '-- Employees list --')
    for name in employees.keys():
        printEmployee(name)

def getEmployeeInfo(oldInfo = None):
    fields = ['phone', 'corporate email', 'job', 'office number', 'skype']
    newInfo = {}
    for field in fields:
        prompt = f'Enter {field}'
        if (oldInfo):
            prompt += f' (current: {oldInfo[field]})'
        value = input(f'{prompt}: ').strip()
        if not value and oldInfo:
            newInfo[field] = oldInfo[field]
        else:
            newInfo[field] = value
    return newInfo

def addEmployee():
    print('\n', '-- Add employee --')
    name = inputName()
    if name in employees:
        print('Employee already exists')
        return
    employees[name] = getEmployeeInfo()
    print('Employee added')

def deleteEmployee():
    print('\n', '-- Delete employee --')
    name = inputName()
    if name in employees:
        del employees[name]
        print('Employee deleted')
    else:
        print('Employee not found')

def findEmployee():
    print('\n', '-- Find employee --')
    name = inputName()
    if name in employees:
        printEmployee(name)
    else:
        print('Employee not found')

def filterEmployees():
    print('\n', '-- Filter employees --')
    field = input('Enter field to filter by (phone, corporate email, job, office number, skype): ').strip().lower()
    value = input('Enter value to filter by: ').strip().lower()
    filtered = filter(
        lambda item: 
            field in item[1] and 
            value in item[1][field].lower(), 
        employees.items())
    for name, _ in filtered:
        printEmployee(name)

def changeEmployeeInfo():
    print('\n', '-- Change employee --')
    name = inputName()
    if name in employees:
        printEmployee(name)
        print()
        employees[name] = getEmployeeInfo(employees[name])
        print('Info changed')
        printEmployee(name)
    else:
        print('Employee not found')

def showMenu():
    print('\n', '-- Base management menu --', '\n')
    print('1. Print all employee')
    print('2. Add employee')
    print('3. Delete employee')
    print('4. Find employee')
    print('5. Filter employees')
    print('6. Change employee info')
    print('0. Exit')

while True:
    showMenu()
    choice = input('\nChoose an action: ').strip()

    if choice == '1':
        printAllEmployees()
    elif choice == '2':
        addEmployee()
    elif choice == '3':
        deleteEmployee()
    elif choice == '4':
        findEmployee()
    elif choice == '5':
        filterEmployees()
    elif choice == '6':
        changeEmployeeInfo()
    elif choice == '0':
        print('The program has ended')
        break
    else:
        print("Incorrect choice, try again")