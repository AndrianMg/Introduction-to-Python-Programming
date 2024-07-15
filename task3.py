def greet_user(name="User"):
    """
    Greets the user with a customizable message.

    Args:
        name (str, optional): The user's name. Defaults to "User".
    """
    print(f"Hello, {name}! Welcome to our platform.")

# Example usage:
greet_user()  # Uses the default name ("User")
greet_user(name="Andrei")  # Customized greeting for Andrei

