
#!/usr/bin/env python3

"""
Provides a reusable function get_numbers() that returns numbers from 1 to 10.
When run directly, it prints the numbers.
"""

def get_numbers() -> list[int]:
    """Return numbers 1 to 10 (inclusive)."""
    return list(range(1, 11))

if __name__ == "__main__":
    for n in get_numbers():
        print(n)

