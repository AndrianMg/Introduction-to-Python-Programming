def combine_arguments(positional_arg, keyword_arg=None, *args, **kwargs):
    """
    Showcase a combination of argument types:
    - positional_arg: A required positional argument.
    - keyword_arg: An optional keyword argument with a default value of None.
    - *args: Variable-length positional arguments (collected as a tuple).
    - **kwargs: Variable-length keyword arguments (collected as a dictionary).
    """
def greet(name, age):
    print(f"Hello, {name}! You are {age} years old.")

greet("Andrei", 30)  # Correct usage

greet(age=30, name="Andrei")  # Correct usage

print(f"Positional argument: {positional_arg}")
print(f"Keyword argument: {keyword_arg}")
print(f"Variable-length positional arguments: {args}")
print(f"Variable-length keyword arguments: {kwargs}")

# Example usage:
combine_arguments("Hello", keyword_arg="World", 1, 2, 3, name="Andrei", age=30)
