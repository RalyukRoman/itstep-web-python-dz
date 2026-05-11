dictionary = {
    'hello': 'bonjour',
    'goodbye': 'au revoir',
    'bread': 'pain',
}

def inputWord(lang):
    name = input(f'Enter the word in {lang}: ')
    return name.strip().lower()

def printDictionary():
    print('\n', '-- English-French dictionary --')
    for wordEnglish, wordFrench in dictionary.items():
        print(f'{wordEnglish} = {wordFrench}')

def addTranslation():
    print('\n', '-- Add translation --')
    word = inputWord('English')
    if word in dictionary:
        print('Translation already exists')
        return
    dictionary[word] = inputWord('French')
    print('Translation added')

def deleteTranslation():
    print('\n', '-- Delete translation --')
    word = inputWord('English')
    if word in dictionary:
        del dictionary[word]
        print('Translation deleted')
    else:
        print('Translation not found')

def findTranslation():
    print('\n', '-- Find translation --')
    word = inputWord('English')
    if word in dictionary:
        print(f'{word} = {dictionary[word]}')
    else:
        print('Translation not found')

def changeTranslation():
    print('\n', '-- Change translation --')
    word = inputWord('English')
    if word in dictionary:
        print(f'{word} = {dictionary[word]}')
        print()
        dictionary[word] = inputWord('French')
        print('Translation changed')
        print(f'{word} = {dictionary[word]}')
    else:
        print('Translation not found')

def showMenu():
    print('\n', '-- Base management menu --', '\n')
    print('1. Print dictionary')
    print('2. Add translation')
    print('3. Delete translation')
    print('4. Find translation')
    print('5. Change translation')
    print('0. Exit')

while True:
    showMenu()
    choice = input('\nChoose an action: ').strip()

    if choice == '1':
        printDictionary()
    elif choice == '2':
        addTranslation()
    elif choice == '3':
        deleteTranslation()
    elif choice == '4':
        findTranslation()
    elif choice == '5':
        changeTranslation()
    elif choice == '0':
        print('The program has ended')
        break
    else:
        print("Incorrect choice, try again")