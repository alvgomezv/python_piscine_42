# Module: Python Fundamentals - Module 00 Basic stuff - Eleven Commandments

## Exercise 00
**Description:** Set up Python and Conda environment.
- This exercise focuses on setting up the Python environment using conda.
- It provides instructions for manually installing conda and creating a Python environment for the module.
- It also provides a script for an automated installation of conda.
- The answers.txt file turned in answers the commands needed for:
  - Output a list of installed packages and their versions.
  - Show the package metadata of numpy.
  - Remove the package numpy.
  - (Re)install the package numpy.
  - Freeze your python packages and their versions in a requirements.txt file you have to turn-in.

**Files to turn in:** `answers.txt` `requirements.txt`

## Exercise 01
**Description:** String Reversal and Letter Case Swap.
- The program takes a string as an argument, reverses it, swaps its letter case, and prints the result.
- It can handle multiple arguments and merges them into a single string.

**Files to turn in:** `exec.py`

## Exercise 02
**Description:** Number Classification (Odd, Even, Zero).
- The program takes a number as an argument and checks whether it is odd, even, or zero.
- It prints the result accordingly.
- It can handle multiple arguments and checks for errors such as non-integer inputs.

**Files to turn in:** `whois.py`

## Exercise 03
**Description:** Text Analyzer (Character Count).
- Part 1 of this exercise involves creating a function called "text_analyzer" that takes a string argument and displays the sums of its uppercase characters, lowercase characters, punctuation characters, and spaces.
- It has error handling for None or non-string inputs.
- Part 2 updates the file to be able to run as a standalone program and uses the "text_analyzer" function.

**Files to turn in:** `count.py`

## Exercise 04
**Description:** Basic Arithmetic Operations.
- The program takes two integers as arguments and performs various arithmetic operations on them, including addition, subtraction, multiplication, division, and modulo.
- It handles errors for incorrect argument counts or non-integer inputs.

**Files to turn in:** `operations.py`

## Exercise 05
**Description:** String Formatting (Kata series).
- This exercise consists of several kata exercises.
- Each exercise focuses on displaying specific data in a specific format.
- The first kata involves displaying numbers from a tuple, the second kata involves displaying information from a dictionary, and so on.
- Each kata has a specific format requirement.

**Files to turn in:** `kata_1.py`, `kata_2.py`, `kata_3.py`

## Exercise 06
**Description:** Recipe Management with Nested Dictionaries.
- Part 1: Create a dictionary called `cookbook` to store recipes.
- Initialize the `cookbook` with 3 recipes, each containing ingredients, meal type, and preparation time.
- Part 2: Create a series of useful functions to handle the `cookbook`, including printing recipe names, printing recipe details, deleting a recipe, and adding a recipe from user input.
- Part 3: Create a command line program that utilizes the `cookbook` and the defined functions.
- The program prompts the user to choose options such as printing the cookbook content, printing a recipe, adding a recipe, deleting a recipe, or quitting the cookbook.

**Files to turn in:** `recipe.py`

## Exercise 07
**Description:** Filter Words.
- The program takes a string `S` and an integer `N` as arguments and prints the list of words in `S` that contain more than `N` non-punctuation characters.
- Words are separated by space characters, and punctuation symbols are removed from the printed list.
- The program must include at least one list comprehension expression.
- If the number of arguments is different from 2 or if the type of any argument is wrong, the program prints an error message.

**Files to turn in:** `filterwords.py`
**Forbidden functions:** `filter`

## Exercise 08
**Description:** Morse Code Encoder.
- The program takes a string as an argument and encodes it into Morse code.
- The program supports space and alphanumeric characters.
- An alphanumeric character is represented by dots `.` and dashes `-`, while a space character is represented by a slash `/`.
- Complete Morse characters are separated by a single space.
- If more than one argument is provided, they are merged into a single string with each argument separated by a space character.
- If no argument is provided, the program does nothing or prints a usage message.

**Files to turn in:** `sos.py`

## Exercise 09
**Description:** Secret Number Guessing Game.
- The program is an interactive guessing game where the user has to guess a number between 1 and 99.
- The program provides feedback if the guess is too high or too low.
- The game ends when the user finds the secret number or types "exit".
- The program counts the number of trials and prints that number when the user wins.
- If the user discovers the secret number on the first try and the secret number is 42, the program makes a reference to Douglas Adams.

**Files to turn in:** `guess.py`

## Exercise 10
**Description:** Loading Bar with Yield Operator.
- Create a function called `ft_progress(lst)` that displays the progress of a for loop.
- The function takes a list as an argument.
- Use the yield operator to generate the progress bar.
- The program demonstrates the usage of the `ft_progress` function with examples.

**Files to turn in:** `loading.py`
**Forbidden functions:** tqdm or any library for automatic loading bar
