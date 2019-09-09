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
	if task == 'n':
		print(number_to_words())
	elif task == 'w':
		print(words_to_number())
	elif task == 'a':
		print(all_wordifications())
	else:
		print("Invalid argument")


if __name__ == '__main__':
	args = sys.argv	
	main(args)