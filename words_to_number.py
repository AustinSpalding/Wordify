# Dictionary mapping a phone keypad
keypad_map = {
	'A': '2',
	'B': '2',
	'C': '2',
	'D': '3',
	'E': '3',
	'F': '3',
	'G': '4',
	'H': '4',
	'I': '4',
	'J': '5',
	'K': '5',
	'L': '5',
	'M': '6',
	'N': '6',
	'O': '6',
	'P': '7',
	'Q': '7',
	'R': '7',
	'S': '7',
	'T': '8',
	'U': '8',
	'V': '8',
	'W': '9',
	'X': '9',
	'Y': '9',
	'Z': '9'
}

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