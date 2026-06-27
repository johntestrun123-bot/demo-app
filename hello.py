"""A simple Python script that greets the user."""
# new change

def greet(name: str) -> str:
    """Return a greeting message."""
    return f"Hello, {name}! Welcome to demo-app."


if __name__ == "__main__":
    user_name = input("What's your name? ")
    print(greet(user_name))
