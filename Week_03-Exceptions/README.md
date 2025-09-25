In Week 3 of CS50P, I learned how to make my programs more robust by anticipating and handling errors gracefully. This week focused on exceptions — a powerful feature in Python that helps prevent programs from crashing when something goes wrong.

What I Learned

- Exceptions - Errors that occur during the execution of a program. Instead of letting the program crash, we can handle these exceptions using specific Python syntax.

- try - Used to wrap code that might raise an exception. If an error occurs, Python jumps to the except block.


- except - Catches and handles specific types of exceptions (like ValueError or RuntimeError).


- else - Runs only if no exceptions were raised in the try block.


- pass - A placeholder that does nothing — useful when you need syntactically valid code but don’t want to take action yet.

- ValueError: Raised when a function receives an argument of the correct type but an inappropriate value
- RuntimeError: A generic error that occurs during program execution.
- Using try/except blocks helps prevent programs from crashing and allows for more user-friendly error messages.
