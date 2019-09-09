from dictionary import *
from keypad_map import *
import itertools

# A helper function to create wordified numbers
# Trims the prefix of a number and wordifies the remaining seven digits
# Returns the first valid wordification if all_words is False, otherwise returns all wordifications found
def wordify(all_words=False, number=None):
	if not number:
		print("Please input a telephone number to wordify")
		number = input()
	number = number.replace('-','')
	if not number.isalnum():
		return "Input contains non-alphanumeric digits"
	while len(number) < 11:
		number = '0' + number
	prefix, suffix = number[:4], number[4:]
	word_arr = []
	word_arr += [keypad_map[n] for n in suffix]
	test_arr = ["".join(word) for word in itertools.product(*word_arr)]
	running = True
	count = 0
	dictionary = get_words()
	words_found = {}
	while running:
		found = False
		for test in test_arr:
			test_word = test[count:].lower()
			if test_word in dictionary:
				found = True
				words_found[test_word.upper()] = test_word.upper()
				break
		if not all_words and found:
			running = False
		else:
			count += 1
			# Remove single letter responses from valid words
			if count >= len(suffix) - 1:
				running = False
	prefix = prefix[0] + '-' + prefix[1:] + '-'
	out = []
	for word in words_found.keys():
		if len(word) == 7:
			out.append(prefix + word)
		else:
			suffix_formatted = suffix[:7 - len(word)] + '-' if len(word) >= 3 else suffix[:4] + '-' + suffix[4:(7 - len(word))] + '-'
			out.append(prefix + suffix_formatted + word)
	return out