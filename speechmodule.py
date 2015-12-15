FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"


def checkio(number):
  num_str = str(number)
  if len(num_str) == 1:
    return FIRST_TEN[number-1]
  elif len(num_str) == 2:
    tens_val = int(num_str[0])
    ones_val = int(num_str[1])
    if number < 20:
      return SECOND_TEN[ones_val]
    elif number % 10:
      return '{} {}'.format(OTHER_TENS[tens_val-2], FIRST_TEN[ones_val-1])
    else:
      return OTHER_TENS[tens_val-2]
  elif len(num_str) == 3:
    huns_val = int(num_str[0])
    tens_val = int(num_str[1])
    ones_val = int(num_str[2])
    if number % 100:
      return '{} hundred {}'.format(FIRST_TEN[huns_val-1], checkio(number%100))
    else:
      return '{} hundred'.format(FIRST_TEN[huns_val-1])

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(4) == 'four', "1st example"
    assert checkio(133) == 'one hundred thirty three', "2nd example"
    assert checkio(12) == 'twelve', "3rd example"
    assert checkio(101) == 'one hundred one', "4th example"
    assert checkio(212) == 'two hundred twelve', "5th example"
    assert checkio(40) == 'forty', "6th example"
    assert not checkio(212).endswith(' '), "Don't forget strip whitespaces at the end of string"
