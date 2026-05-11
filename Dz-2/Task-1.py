players = {
    'Michael Jordan': {
        'height': 198 
    },
    'LeBron James': {
        'height': 206 
    },
    'Stephen Curry': {
        'height': 188 
    },
}

def inputName():
    name = input('Enter full name: ')
    return name.strip().title()

def printPlayer(name):
    info = players[name]
    print(f'\n{name}: ')
    for key, value in info.items():
        print(f'  {key} = {value}')

def printAllPlayers():
    print('\n', '-- Players list --')
    for name in players.keys():
        printPlayer(name)

def getPlayerInfo():
    height = input('Enter height (cm): ')
    if height.isdigit():
        return {
            'height': int(height.strip())
        }
    else:
        print('Invalid input')

def addPlayer():
    print('\n', '-- Add player --')
    name = inputName()
    if name in players:
        print('Player already exists')
        return
    info = getPlayerInfo()
    if info:
        players[name] = info
        print('Player added')

def deletePlayer():
    print('\n', '-- Delete player --')
    name = inputName()
    if name in players:
        del players[name]
        print('Player deleted')
    else:
        print('Player not found')

def findPlayer():
    print('\n', '-- Find player --')
    name = inputName()
    if name in players:
        printPlayer(name)
    else:
        print('Player not found')

def filterPlayers():
    print('\n', '-- Filter players --')
    field = input('Enter field to filter by (height): ').strip().lower()
    value = input('Enter value to filter by: ').strip().lower()
    filtered = filter(
        lambda item: 
            field in item[1] and 
            value in item[1][field].lower(), 
        players.items())
    for name, _ in filtered:
        printPlayer(name)

def changePlayerInfo():
    print('\n', '-- Change player --')
    name = inputName()
    if name in players:
        printPlayer(name)
        print()
        info = getPlayerInfo()
        if info:
            players[name] = info
            print('Info changed')
            printPlayer(name)
    else:
        print('Player not found')

def showMenu():
    print('\n', '-- Base management menu --', '\n')
    print('1. Print all player')
    print('2. Add player')
    print('3. Delete player')
    print('4. Find player')
    print('5. Filter players')
    print('6. Change player info')
    print('0. Exit')

while True:
    showMenu()
    choice = input('\nChoose an action: ').strip()

    if choice == '1':
        printAllPlayers()
    elif choice == '2':
        addPlayer()
    elif choice == '3':
        deletePlayer()
    elif choice == '4':
        findPlayer()
    elif choice == '5':
        filterPlayers()
    elif choice == '6':
        changePlayerInfo()
    elif choice == '0':
        print('The program has ended')
        break
    else:
        print("Incorrect choice, try again")