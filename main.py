import sys
from number_to_words import *
from words_to_number import *
from all_wordifications import *

def main(args):
	task = None
	if len(args) == 1:
		print("To convert to a pure number, wordified number, or to see all possible words please type 'n', 'w', or 'a' respectively")
		task = input()
	else:
		task = args[1]
	number = args[2] if len(args) > 2 else None
	if task == 'w':
		print(number_to_words(number))
	elif task == 'n':
		print(words_to_number(number))
	elif task == 'a':
		print(all_wordifications(number))
	else:
		print("Invalid argument")


if __name__ == '__main__':
	args = sys.argv	
	main(args)