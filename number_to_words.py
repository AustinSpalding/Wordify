from wordify import *
import sys

# Returns the first, lengthiest valid wordification of a number
def number_to_words(number=None):
	if number:
		return wordify(False, number)
	else:
		return wordify()

if __name__ == '__main__':
	args = sys.argv
	number = args[1] if len(args) > 1 else None
	number_to_words(number)