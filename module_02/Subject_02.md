# Module:Python Fundamentals - Module 02 Basics 3

## Exercise 00:
**Description:**
- The goal of this exercise is to work on the built-in functions `map`, `filter`, and `reduce`. 
- You will implement your own versions of these functions: `ft_map`, `ft_filter`, and `ft_reduce`.
- Take the time to understand the use cases of these built-in functions and the `reduce` function in the `functools` module.
- You are not expected to code specific classes to create `ft_map`, `ft_filter`, or `ft_reduce` objects.

**Files to turn in:** `ft_map.py`, `ft_filter.py`, `ft_reduce.py`
**Forbidden functions:** `map`, `ilter`, `reduce`

## Exercise 01:
**Description:**
- The objective of this exercise is to discover and manipulate `*args` and `**kwargs` arguments.
- You need to implement a function named `what_are_the_vars` that returns an instance of the `ObjectC` class.
- The attributes of the `ObjectC` instance should be set based on the parameters received during instantiation.
- You will have to modify the `instance` of `ObjectC`, not the class itself.
- Take a look at the `getattr` and `setattr` built-in functions to help you accomplish this task.

**Files to turn in:** `main.py`

## Exercise 02:
**Description:**
- In this exercise, you will learn about decorators, specifically the `@log` decorator.
- The `@log` decorator will write information about the decorated function to a `machine.log` file.
- Pay attention to the different actions logged when each method is called.
- The log file should also include the username from the environment variable.

**Files to turn in:** `logger.py`

## Exercise 03:
**Description:**
- The goal of this exercise is to implement a context manager as a class for handling CSV files.
- You need to create a class named `CsvReader` that serves as a context manager.
- The `CsvReader` class should open, read, and parse a CSV file.
- The class should have the following built-in methods: `__init__`, `__enter__`, and `__exit__`.
- It is mandatory to close the file once the process has completed.
- You should handle badly formatted CSV files, such as a mismatch between the number of fields and records or records with different lengths.

**Files to turn in:** `csvreader.py`

## Exercise 04:
**Description:**
- The goal of this exercise is to create a package named `my_minipack` and understand the process of building and installing packages.
- The package should include two modules: `progress` and `logger`.
- The package should be installed using `pip` by running one of the following commands:
  - `pip install ./dist/my_minipack-1.0.0.tar.gz`
  - `pip install ./dist/my_minipack-1.0.0-py3-none-any.whl`
- Additionally, create a `LICENSE.md` file and a `README` file to provide documentation about your library.

**Files to turn in:** `build.sh`, `*.py`, `*.md`, `*.cfg`, `*.txt`

## Exercise 05:
**Description:**
- The goal of this exercise is to create a class named `TinyStatistician` that implements basic statistical methods.
- The class should have the following methods: `mean`, `median`, `quartiles`, `var`, and `std`.
- The methods should perform calculations on a given non-empty list or array.
- The class should handle empty lists or arrays appropriately and return `None

**Files to turn in:** `TiniStatistician.py`
**Forbidden functions:** Any function that calculates mean, median, quartiles, variance, or standard deviation for you.



