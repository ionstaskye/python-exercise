def print_upper_words(list):

    for word in list:
        print(word.upper())
def must_start_with_e(list):

    for word in list:
        if word.startswith("e") or word.startswith("E"):
            print (word.upper())

def must_start_with(word, must_start):

    for words of word:
        for letter in must_start:
            if word.startswith(letter):
                print(word.upper())

