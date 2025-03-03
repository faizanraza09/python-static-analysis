"""This module demonstrates basic functions for arithmetic and greetings."""

def add_numbers(first: int, second: int) -> int:
    """Adds two numbers together.
    
    Args:
        first: First number
        second: Second number
        
    Returns:
        The sum of first and second number
    """
    return first + second


def hello(name: str) -> None:
    """Prints a greeting message.
    
    Args:
        name: The name to greet
    """
    print(f"Hello, {name}!")


hello("Alice")
