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
# Sources
NLTK's English language library