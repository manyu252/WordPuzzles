Supports only MacOS and Linux.
<!-- Windows support will come soon. -->

# Usage
To run the code for wordle, double click the ```wordle_helper.command``` file.

To run the code for spelling bee, double click the ```spelling_bee.command``` file.

# wordle_helper
This code aims to assist you to find legitimate words when a few characters are missing.
One can use this to play word games like wordle, quordle etc.

## Steps:
1. Inside the project folder, execute -
```bash
python3 wordle_helper.py
```
_Note: You can run in both python2 and python3_

2. It will prompt you to enter an incomplete word. Put an underscore `_` wherever you don't know which alphabet will occur. For example: `c_t_`
3. Give including/omitting alphabet conditions, if any. For example: `inclue alphabet: ue`, `omit alphabet: y`. This will include `u` and `e` in the output words and will omit `y` in the output words.
4. You will get the return value of all possible words that can occur with your combination.

# spelling_bee
This code will give you solution of spelling bee for upto 5 letter words.

## Steps:
1. Inside the project folder, execute -
```bash
python3 spelling_bee.py
```
_Note: You can run in both python2 and python3_

2. It will prompt you to enter the `necessary letter` (the one in the middle of spelling_bee which is always required).
3. Now give all the other surrounding letters.
4. Now enter the minimum and maximum length of string you require. It is advised to **NOT** give max greater than 5.
4. You will get the return value of all possible words that can occur with your combination.