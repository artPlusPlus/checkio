import math

def checkio(opacity):
	def is_fib(age):
		"""
		totally cribbed from SO
		http://stackoverflow.com/questions/21800940/function-to-check-whether-a-number-is-a-fibonacci-number-or-not
		"""
		if age == 0:
			return True
		phi = 0.5 + 0.5 * math.sqrt(5.0)
	    a = phi * age
	    return abs(round(a) - a) < 1.0 / age

    age = 0
    _opacity = 10000
    while _opacity != opacity:
    	age += 1
    	if is_fib(age):
    		_opacity -= age
    	else:
    		_opacity += 1
    return age
    	

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(10000) == 0, "Newborn"
    assert checkio(9999) == 1, "1 year"
    assert checkio(9997) == 2, "2 years"
    assert checkio(9994) == 3, "3 years"
    assert checkio(9995) == 4, "4 years"
    assert checkio(9990) == 5, "5 years"