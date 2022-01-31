def letter_at_pos(words, letter, pos):
    words_list_sorted = [idx for idx in words if idx[pos].lower() == letter.lower()]

    return words_list_sorted


def letter_not_at_pos(words, letter, pos):
    words_list_sorted = [idx for idx in words if idx[pos].lower() != letter.lower()]

    return words_list_sorted


def letter_in(words, letter):
    words_list_sorted = [idx for idx in words if letter.lower() in idx.lower()]

    return words_list_sorted


def letter_not_in(words, letter):
    words_list_sorted = [idx for idx in words if letter.lower() not in idx.lower()]

    return words_list_sorted


def show_words(words):
    msg = f"Available Words: {len(words)} \n"
    x = 0
    for word in words:
        msg += word + " "
        x += 1

        if x % 10 == 0:
            msg += "\n"

    print(msg)


def show_commands():
    print("1. Letter with position")
    print("2. Letter not at this position (Do Letter without position at the same time)")
    print("3. Letter without position")
    print("4. Letter not in the word")
    print("5. Show available words")
    print("6. Done")


# Chargement des mots
with open('words.txt', 'r') as file:
    words_list = file.read().split(' ')

# Récupération de la première lettre
first_letter_ok = False
first_letter = None

while not first_letter_ok:
    first_letter = input("Enter the first letter\n")
    if len(first_letter) == 1 and first_letter.isalpha():
        first_letter_ok = True

# Recherche des mots commençant par la lettre donné
words_with_first_letter = [idx for idx in words_list if idx[0].lower() == first_letter.lower()]

done = False
available_words = words_with_first_letter

while not done:
    show_commands()

    command = int(input("Choose a command\n"))

    if command == 1:
        letter = input("Letter ?\n")
        pos = int(input("Position ?\n"))
        available_words = letter_at_pos(available_words, letter, pos)

    if command == 2:
        letter = input("Letter ?\n")
        pos = int(input("Position ?\n"))
        available_words = letter_not_at_pos(available_words, letter, pos)
        available_words = letter_in(available_words, letter)

    elif command == 3:
        letter = input("Letter ?\n")
        available_words = letter_in(available_words, letter)

    elif command == 4:
        letter = input("Letter ?\n")
        available_words = letter_not_in(available_words, letter)

    elif command == 5:
        show_words(available_words)

    elif command == 6:
        print("Bye !")
        done = True

    else:
        print("Unknown Command !")






















