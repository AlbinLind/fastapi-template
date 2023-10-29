"""Utiliti functions that are used by tests."""
import random
import string

def generate_random_string(length: int = 10) -> str:
    """Generate a random string of a given length."""

    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))