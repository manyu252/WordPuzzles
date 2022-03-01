# find_words
This project aims to assist you to find legitimate words when a few characters are missing.
One can use this to play word games like wordle, quordle, spelling bee etc.

## Steps:
1. git clone this repo
2. Inside the project folder, execute -
```bash
python find_words.py
```
_Note: You can run in both python2 and python3_

3. It will prompt you to enter an incomplete word. Put an underscore `_` wherever you don't know which alphabet will occur. For example: `c_t` will return the output `['cot', 'cit', 'cat', 'cut']`
4. You will get the return value of all possible words that can occur with your combination.