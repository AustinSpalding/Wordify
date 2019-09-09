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
Running `python main.py <task> <number>`, where <task> is `n`, `w`, or `a` converts to a pure number, a wordy number, or a list of possible wordy numbers respectively. The <number> placeholder should be replaced with an 11-digit U.S. standard telephone number, with or without dashes. Alternatively entering `python main.py <task>` or just `python main.py` begins a series of commandline prompts. Following the directions will provide the necessary information to run.

Finally, running `python number_to_words.py`, `python all_wordifications.py`, or `python words_to_number.py` with or without the following number will also work, and again will prompt additional info as needed.

Note that only the local number (final seven digits) will be wordified due to the significance of some area codes. Running all_wordifications will take some time due to dictionary size and the number of possible wordifications. 
# Sources
[NLTK](https://www.nltk.org)'s English language library