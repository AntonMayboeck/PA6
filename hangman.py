import random

def get_wordlist():
    word_list = []
    with open("word_bank", "r") as word_bank:
        for line in word_bank:
            for char in line.split():
                word_list.append(char)
    return word_list

def random_word(wordlist):
    random_word = random.choice(wordlist)
    return random_word

def add_word(word):
    try:
        if word.isalpha():
            with open("word_bank", "a") as words:
                words.write(" " + word)
    except AttributeError :
        return print("Please only letters")
a = get_wordlist()
b = random_word(a)
c = add_word(1)
print(a)
print(b)
print(a)