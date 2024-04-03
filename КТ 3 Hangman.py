#Игра виселица

import random

HANGMAN = ("""


|\
|_\_____""", """
|
|
|
|
|
|
|
|\
|_\_____""", """
------.
|     |
|
|
|
|
|
|
|\
|_\_____""", """
------.
|     |
|     O
|
|
|
|
|
|\
|_\_____""", """
------.
|     |
|     O
|    /|\\
|
|
|
|
|\
|_\_____""", """
------.
|     |
|     O
|    /|\\
|    |||
|
|
|
|\
|_\_____""", """
------.
|     |
|     O
|    /|\\
|    |||
|     |
|
|
|\
|_\_____""", """
------.
|     |
|     O
|    /|\\
|    |||
|     |
|    | |
|    | |
|\
|_\_____
""")

MAX_WRONG = len(HANGMAN) - 1

WORDS = ("РУСОФОБ", "ХРЮКАЮЩИЙПОДСВИНОК", "ГОЙДА", "СЛОНЯРА", "ДЕНАЦИФИКАЦИЯ")
#инициализация переменных
word = random.choice(WORDS) #слово для отгадывания

so_far = "-" * len(word) #по одному дефису на каждую букву, которую надо отгадать

wrong = 0 #кол-во ошибок

used = [] #буквы, которые игрок уже предлагал

while wrong < MAX_WRONG and so_far != word:
    print(HANGMAN[wrong])
    print("\nВы уже пердлагали следующие буквы:\n", used)
    print("\nОтгаданное вами слово, сейчас выглядит так:\n", so_far)
    guess = input("\n\nВведите букву: ")
    guess = guess.upper()

    while guess in used:
        print("Вы уже предлагали букву", guess)
        guess = input("\n\nВведите букву: ")
        guess = guess.upper()
    used.append(guess)

    if guess in word:
        print("\nДа! Буква", guess, "есть в слове!")
        #Новая строка so_far с отгаданной буквой или буквами
        new = ""
        for i in range(len(word)):
            if guess == word[i]:
                new += guess
            else:
                new += so_far[i]
        so_far = new
    else:
        print("\nК сожалению, буквы", guess, "нет в слове.")
        wrong += 1
if wrong == MAX_WRONG:
    print(HANGMAN[wrong])
    print("\nВас повесили!")
else:
    print("\nВы отгадали!")
print("\nБыло загадано слово", word)
input("\n\nНажмите Enter, чтобы выйти.")

print(WORDS)
