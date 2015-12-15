import re
import string


def checkio(text):
    text = text.lower()
    chars = string.ascii_lowercase
    chars = sorted([(text.count(c), c) for c in set(text) if c in chars])
    while len(chars) > 1 and chars[-1][0] == chars[-2][0]:
        chars.pop()
    return chars[-1][1]

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")
