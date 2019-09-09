# Wordify
Wordify converts phone numbers to a number followed by a keymapped word (i.e. 1-800-724-6837 -> 1-800-PAINTER), and standardizes wordy numbers.
## Getting Started
### Prerequisites
These functions require Python 3.5+ and Pip
### Installing
1. Install depencencies with pip using `pip install -r requirements.txt`
2. If using the provided English dictionary, run `python setup.py` and download 'Words' under the 'Corpora' tab
### Customizing
To use your own dictionary, edit words() in dictionary.py to return a list of words from your selected source. Custom keymaps require editing keypad_map.py.
## Use
Running `python main.py` begins a series of commandline prompts. Following the directions leads to one of the three core functions which will then prompt you for either a pure or wordified number. Any 11-digit U.S. standard telephone number may be entered, with or without dashes. Note that only the local number (final seven digits) will be wordified due to the significance of some area codes. Running all_wordifications will take some time due to dictionary size and the number of possible wordifications. 
# Sources
[NLTK](https://nltk.org)'s English language library