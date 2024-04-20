#Игра виселица
import random
import sys
#Переменные
WORDS = ("РУСОФОБ", "ПОДСВИНОК", "ГОЙДА", "СЛОНЯРА", "ДЕНАЦИФИКАЦИЯ")
word = random.choice(WORDS) #слово для отгадывания
so_far = "-" * len(word) #по одному дефису на каждую букву, которую надо отгадать
wrong = 0 #кол-во ошибок
MAX_WRONG = 6 #максимальное кол-во ошибок
used = [] #буквы, которые игрок уже предлагал
letter = None #буква, которую игрок предлагает

def check_wrongs_and_print_hangman():
    global wrong
    global MAX_WRONG
    global so_far
    global word
    while wrong < MAX_WRONG:
        wrong += 1
        if wrong == 1:
            print_hangman_1()
        elif wrong == 2:
            print_hangman_2()
        elif wrong == 3:
            print_hangman_3()
        elif wrong == 4:
            print_hangman_4()
        elif wrong == 5:
            print_hangman_5()
        elif wrong == 6:
            print_hangman_6()
        break
def print_hangman_1():
    with open(r'C:\Users\zapev\PycharmProjects\Python КТ 3\Hangman\hangman-1.txt', 'r') as file:
        # Читаем содержимое файла
        file_contents = file.read()
        # Выводим содержимое файла
        print(file_contents)

def print_hangman_2():
    with open(r'C:\Users\zapev\PycharmProjects\Python КТ 3\Hangman\hangman-2.txt', 'r') as file:
        # Читаем содержимое файла
        file_contents = file.read()
        # Выводим содержимое файла
        print(file_contents)

def print_hangman_3():
    with open(r'C:\Users\zapev\PycharmProjects\Python КТ 3\Hangman\hangman-3.txt', 'r') as file:
        # Читаем содержимое файла
        file_contents = file.read()
        # Выводим содержимое файла
        print(file_contents)

def print_hangman_4():
    with open(r'C:\Users\zapev\PycharmProjects\Python КТ 3\Hangman\hangman-4.txt', 'r') as file:
        # Читаем содержимое файла
        file_contents = file.read()
        # Выводим содержимое файла
        print(file_contents)
def print_hangman_5():
    with open(r'C:\Users\zapev\PycharmProjects\Python КТ 3\Hangman\hangman-5.txt', 'r') as file:
        # Читаем содержимое файла
        file_contents = file.read()
        # Выводим содержимое файла
        print(file_contents)

def print_hangman_6():
    with open(r'C:\Users\zapev\PycharmProjects\Python КТ 3\Hangman\hangman-6.txt', 'r') as file:
        # Читаем содержимое файла
        file_contents = file.read()
        # Выводим содержимое файла
        print(file_contents)
def message_input():
    global letter
    letter = input("\nВведите букву: ")
    letter = letter.upper()
    check_letter()

def message_status():
    print("\nВы уже пердлагали следующие буквы:\n", used)
    print("\nОтгаданное вами слово, сейчас выглядит так:\n", so_far)
    message_input()

def message_open_show_letter_in_word():
    global so_far  # объявляем so_far как глобальную переменную
    # Новая строка so_far с отображением отгаданных букв
    new = ""
    for i in range(len(word)):
        if letter == word[i]:
            new += letter
        else:
            new += so_far[i]
    so_far = new
    check_win()
    message_status()  #Вывод данных

def check_letter_to_be_char():
    if len(letter) != 1:
        print("Введите один символ!")
        message_input()

def check_rus_letter(): #Проверка на русский символ
    if 'а' <= letter <= 'я' or 'А' <= letter <= 'Я':
        print("Это кириллическая буква.")

def check_eng_letter(): #Проверка на латинский символ
    if 'a' <= letter <= 'z' or 'A' <= letter <= 'Z':
        print("Это латинская буква.")

def check_win():
    # Проверка на выигрыш
    if wrong == MAX_WRONG:  # Если ошибки = максимуму ошибок
        print("\nВы проиграли! Было загадано слово:", word)
        sys.exit()  # Закончить выполенине
    elif so_far == word:  # Если слово отгадано
        print("\nВы выиграли! Было загадано слово:", word)
        sys.exit()  # Закончить выполенине
    # Если ошибки не = максимуму ошибок и слово не отгадано
    else:
        message_status()
def check_letter(): #Проверка введенного символа
    global wrong, used, word, MAX_WRONG, so_far, letter
    #Проверка на единственный символ
    if len(letter) != 1:
        print("Введите один символ!")
        message_input()
    else:
        #Проверка на русскую букву
        if not ('а' <= letter <= 'я' or 'А' <= letter <= 'Я'):
            print("Это не кириллическая буква!")
            message_input()
        else:
            #Проверка на уже введенную букву
            if letter in used: #Если буква уже вводилась
                print("Вы уже предлагали букву", letter)
                message_input()
            else:  # Если буква вводится впервые
                used.append(letter)  # Добавляем букву в список использованных
                if letter in word:  # Буква есть в слове
                    print("\nДа! Буква", letter, "есть в слове!")
                    message_open_show_letter_in_word()
                else:  # Буквы нет в слове
                    print("\nК сожалению, буквы", letter, "нет в слове.")
                    print("\nУ вас осталось", MAX_WRONG - 1 - wrong, "попыток.")
                    check_wrongs_and_print_hangman()
                    message_open_show_letter_in_word()

message_status()


