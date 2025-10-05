# Python Concepts Summary

This README provides a summary of key Python programming concepts that were explored during the development of a password manager project, which served as the final project for the CS50 course. Note: There are no files in this folder because the project was in progress.

## Object-Oriented Programming (OOP)
OOP is a programming paradigm based on the concept of objects, which can contain data and code to manipulate that data. It promotes modularity, reusability, and encapsulation.

### Classes
Classes are blueprints for creating objects. They encapsulate data for the object and methods to manipulate that data.

### `raise`
The `raise` statement is used to trigger exceptions manually, allowing for custom error handling.

### Class Methods
Class methods are methods that operate on the class itself rather than instances. They are defined using the `@classmethod` decorator.

### Static Methods
Static methods are utility functions that belong to a class but do not access or modify class or instance data. They are defined using the `@staticmethod` decorator.

### Inheritance
Inheritance allows a class to inherit attributes and methods from another class, promoting code reuse and hierarchical relationships.

### Operator Overloading
Operator overloading enables custom behavior for standard operators (like `+`, `-`, `==`) when used with class instances.

## Global Variables
Global variables are accessible throughout the entire program. They should be used sparingly to avoid unintended side effects.

## Constants
Constants are variables that should not change once assigned. By convention, they are written in uppercase (e.g., `MAX_SIZE = 100`).

## Type Hints
Type hints provide information about the expected data types of variables and function parameters, improving code readability and tooling support.

## Docstrings
Docstrings are string literals used to document modules, classes, functions, and methods. They help explain the purpose and usage of code components.

## `argparse`
The `argparse` module is used to parse command-line arguments, enabling dynamic input and configuration for Python scripts.

## Unpacking
Unpacking allows multiple variables to be assigned from a sequence in a single statement (e.g., `a, b = [1, 2]`).

## `*args` and `**kwargs`
- `*args` allows a function to accept any number of positional arguments.
- `**kwargs` allows a function to accept any number of keyword arguments.

## `map`
The `map` function applies a given function to each item in an iterable, returning a map object.

## List Comprehension
List comprehensions provide a concise way to create lists using a single line of code.

## `filter`
The `filter` function filters elements from an iterable based on a function that returns `True` or `False`.

## Dictionary Comprehension
Similar to list comprehensions, dictionary comprehensions allow for the creation of dictionaries in a concise manner.

## `enumerate`
The `enumerate` function adds a counter to an iterable, returning pairs of index and value.

## Generators and Iterators
- Generators are functions that yield values one at a time using the `yield` keyword.
- Iterators are objects that implement the iterator protocol (`__iter__` and `__next__`), allowing for iteration over data.

