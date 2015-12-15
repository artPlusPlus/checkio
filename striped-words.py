import re


VOWELS = "AEIOUY"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"


def checkio(text):
    text = text.upper()
    words = []
    striped_words = []
    while text:
    	garbage_match = re.match('(?P<garbage>\W*).*', text)
    	garbage = garbage_match.group('garbage')
    	if garbage:
    		text = text.replace(garbage, '', 1)
    		continue

    	word_match = re.match('(?P<word>\w*).*', text)
    	word = word_match.group('word')
    	if word:
    		if len(word) > 1:
    			words.append(word)
    		text = text.replace(word, '', 1)

    for word in words:
    	if word[0] in VOWELS:
    		buckets = [VOWELS, CONSONANTS]
    	else:
    		buckets = [CONSONANTS, VOWELS]
    	striped = all([char in buckets[idx % 2] for idx, char in enumerate(word)])
    	if striped:
    		striped_words.append(word)

    return len(striped_words)

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("My name is ...") == 3, "All words are striped"
    assert checkio("Hello world") == 0, "No one"
    assert checkio("A quantity of striped words.") == 1, "Only of"
    assert checkio("Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human"
