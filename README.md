# find_words
This project aims to assist you to find legitimate words when a few characters are missing.
One can use this to play word games like wordle, quordle, spelling bee etc.

## Steps:
1. Inside the project folder, execute -
```bash
python find_words.py
```
_Note: You can run in both python2 and python3_

2. It will prompt you to enter an incomplete word. Put an underscore `_` wherever you don't know which alphabet will occur. For example: `c_t_`
3. Give including/omitting alphabet conditions, if any. For example: `inclue alphabet: ue`, `omit alphabet: y`. This will include `u` and `e` in the output words and will omit `y` in the output words.
4. You will get the return value of all possible words that can occur with your combination.