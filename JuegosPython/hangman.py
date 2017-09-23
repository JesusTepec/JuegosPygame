import random
HANGMANPICS = ['''

  +---+
  |   |
      |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
words = '''aguila alce almeja araña babuino ballena buho burro cabra camello
carnero castor cebra ciervo cisne cobra comadreja conejo coyote cuervo delfin
elefante foca ganso gato halcon hormiga huron lagarto leon lobo loro llama
mono mula murcielago nutria oso oveja paloma panda pato pavo perro perezoso
piton puma rata raton rana rinoceronte salmon sapo serpiente sigueña tejon
tiburon tigre topo tortuga triton trucha zorrillo zorro'''.split()


def getRandomWord(wordList):
    # This function returns a random string from the passed list of strings.
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]


def displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord):
    print(HANGMANPICS[len(missedLetters)])
    print()

    print('Letras usadas:', end=' ')

    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secretWord)
    #replace blanks with correctly guessed letters
    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i + 1:]
    # show the secret word with spaces in between each letter
    for letter in blanks:
        print(letter, end=' ')
    print()


def getGuess(alreadyGuessed):
    # Returns the letter the player entered. This function makes sure the player entered a single letter, and not something else.
    while True:
        print('Adivina una letra.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Por favor ingresa solo una letra.')
        elif guess in alreadyGuessed:
            print('Ya has usado esa letra. Elija de nuevo')
        elif guess not in 'abcdefghijklmnñopqrstuvwxyz':
            print('Por favor ingrese una LETRA.')
        else:
            return guess


def playAgain():
    # This function returns True if the player wants to play again, otherwise it returns False.
    print('Quieres juegar otra vez? (yes or no)')
    return input().lower().startswith('y')


print('A H O R C A D O')
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameIsDone = False

while True:
    displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)

    # Let the player type in a letter.
    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        # Check if the player has won
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('Si! La palabra secreta es "' + secretWord + '"! Ganaste')
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess

        # Check if player has guessed too many times and lost
        if len(missedLetters) == len(HANGMANPICS) - 1:
            displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)
            print('Se ta han terminda los intentos!\nDespues de d' +
            str(len(missedLetters)) +
            ' intentos fallidos y ' +
            str(len(correctLetters)) +
            ' aciertos, la palabra era "' +
            secretWord + '"')
            gameIsDone = True

    # Ask the player if they want to play again (but only if the game is done).
    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord = getRandomWord(words)
        else:
            break
