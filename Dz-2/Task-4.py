books = {
    '1984': {
        'author': 'George Orwell',
        'genre': 'Dystopia',
        'year': '1949',
        'pages': '328',
        'publisher': 'Secker & Warburg' 
    },
    'The Hobbit': {
        'author': 'J.R.R. Tolkien',
        'genre': 'Fantasy',
        'year': '1937',
        'pages': '310',
        'publisher': 'Allen & Unwin' 
    }
}

def inputTitle():
    title = input('Enter title: ')
    return title.strip().title()

def printBook(title):
    info = books[title]
    print(f'\n{title}: ')
    for key, value in info.items():
        print(f'  {key} = {value}')

def printAllBooks():
    print('\n', '-- Books list --')
    for title in books.keys():
        printBook(title)

def getBookInfo(oldInfo = None):
    fields = ['author', 'genre', 'year', 'pages', 'publisher']
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

def addBook():
    print('\n', '-- Add book --')
    title = inputTitle()
    if title in books:
        print('Book already exists')
        return
    books[title] = getBookInfo()
    print('Book added')

def deleteBook():
    print('\n', '-- Delete book --')
    title = inputTitle()
    if title in books:
        del books[title]
        print('Book deleted')
    else:
        print('Book not found')

def findBook():
    print('\n', '-- Find book --')
    title = inputTitle()
    if title in books:
        printBook(title)
    else:
        print('Book not found')

def filterBooks():
    print('\n', '-- Filter books --')
    field = input('Enter field to filter by (author, genre, year, pages, publisher): ').strip().lower()
    value = input('Enter value to filter by: ').strip().lower()
    filtered = filter(
        lambda item: 
            field in item[1] and 
            value in item[1][field].lower(), 
        books.items())
    for title, _ in filtered:
        printBook(title)

def changeBookInfo():
    print('\n', '-- Change book --')
    title = inputTitle()
    if title in books:
        printBook(title)
        print()
        books[title] = getBookInfo(books[title])
        print('Info changed')
        printBook(title)
    else:
        print('Book not found')

def showMenu():
    print('\n', '-- Base management menu --', '\n')
    print('1. Print all books')
    print('2. Add book')
    print('3. Delete book')
    print('4. Find book')
    print('5. Filter books')
    print('6. Change book info')
    print('0. Exit')

while True:
    showMenu()
    choice = input('\nChoose an action: ')

    if choice == '1':
        printAllBooks()
    elif choice == '2':
        addBook()
    elif choice == '3':
        deleteBook()
    elif choice == '4':
        findBook()
    elif choice == '5':
        filterBooks()
    elif choice == '6':
        changeBookInfo()
    elif choice == '0':
        print('The program has ended')
        break
    else:
        print("Incorrect choice, try again")