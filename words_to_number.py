from keypad_map import *
import sys

# Reverts a 10 digit wordified number to a standard US phone number
def words_to_number(word=None):
	if not word:
		print("Please input a wordified telephone number to convert")
		word = input()
	word = word.replace('-','')
	if not word.isalnum():
		return "Input contains non-alphanumeric digits"
	while len(word) < 11:
		word = '0' + word
	word = word.upper()
	number = ""
	number = [number + char if char.isdigit() else number + keypad_map[char] for char in word]
	number = "".join(number)
	return number[0] + '-' + number[1:4] + '-' + number[4:7] + '-' + number[7:]

if __name__ == '__main__':
	args = sys.argv
	number = args[1] if len(args) > 1 else None
	words_to_number(number)