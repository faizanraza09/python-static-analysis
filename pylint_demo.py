"""This module demonstrates basic functions for arithmetic and greetings."""

def add_numbers(a: int, b: int) -> int:
    """Adds two numbers together.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        The sum of a and b
    """
    return a + b


def hello(name: str) -> None:
    """Prints a greeting message.
    
    Args:
        name: The name to greet
    """
    print(f"Hello, {name}!")


hello("Alice")
