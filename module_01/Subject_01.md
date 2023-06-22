# Module: Python Fundamentals - Module 01 Basic 2

## Exercise 00:
**Description:**
- Create two classes, Book and Recipe, to familiarize yourself with the notions of classes and object manipulation.
- The Book class has attributes such as name, last_update, creation_date, and recipes_list.
- The Recipe class has attributes like name, cooking_lvl, cooking_time, ingredients, description, and recipe_type.
- Implement methods to initialize objects, check values, and perform operations on the classes.
- Write a test.py file to test the functionality of your classes.

**Files to turn in:** `book.py`, `recipe.py`, `test.py`

## Exercise 01: 
**Description:**
- Explore the concept of inheritance by creating a GotCharacter class and a child class representing a specific house from the Game of Thrones (GoT) series.
- The GotCharacter class has attributes such as first_name and is_alive.
- The child class inherits these attributes and adds family_name and house_words.
- Implement methods to print the house words and change the character's status.
- A test.py file will be provided to verify the correctness of your implementation.

**Files to turn in:** `game.py`

## Exercise 02:
**Description:**
- Create a Vector class that allows mathematical operations with vectors.
- The class can represent both column vectors and row vectors, storing the vector values and their shape.
- Implement methods to perform dot product and transpose operations on vectors.
- A test.py file will be provided to validate the functionality of your Vector class.

**Files to turn in:** `vector.py`, `test.py`

## Exercise 03:
**Description:**
Code a function called generator that takes a text as input (only printable characters), uses the string parameter sep as a splitting parameter, and yields the resulting substrings. The function can take an optional argument. The options are:
- shuffle: shuffles the list of words
- unique: returns a list where each word appears only once
- ordered: alphabetically sorts the words.

**Files to turn in:** `generator.py`
**Forbidden functions:** `random.shuffle`, `random.sample`

## Exercise 04:
**Description:**
- Code a class Evaluator that has two static functions named zip_evaluate and enumerate_evaluate.
- The goal of these two functions is to compute the sum of the lengths of every word of a given list weighted by a list of coefficients coefs.
- The lists coefs and words have to be the same length. If this is not the case, the function should return -1.

**Files to turn in:** `eval.py`
**Forbidden functions:** `while`

## Exercise 05:
**Description:**
Code a class named Bank that handles the security part of each transfer attempt. The Bank class checks if the Account is the right object, not corrupted, and stores enough money to complete the transfer. A corrupted bank account has:
- an even number of attributes
- an attribute starting with "b"
- no attribute starting with "zip" or "addr"
- no attribute "name", "id", and "value"
- "name" not being a string
- "id" not being an int
- "value" not being an int or a float.

**Files to turn in:** `the_bank.py`
