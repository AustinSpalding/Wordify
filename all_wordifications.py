from wordify import *

# Returns a list of all valid wordifications of a number
def all_wordifications(number=False):
	if number:
		return wordify(True, number)
	else:
		return wordify(True)

if __name__ == '__main__':
	args = sys.argv
	number = args[1] if len(args) > 1 else None
	number_to_words(number)