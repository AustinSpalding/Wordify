from keypad_map import *

# Reverts a 10 digit wordified number to a standard US phone number
def words_to_number():
	print("Please input a wordified telephone number to convert")
	word = input()
	word.replace('-','')
	if not word.isalnum():
		return "Input contains non-alphanumeric digits"
	word = word.upper()
	number = ""
	number = [number + char if char.isdigit() else number + keypad_map[char] for char in word]
	number = "".join(number)
	return number[0] + '-' + number[1:4] + '-' + number[4:7] + '-' + number[7:]