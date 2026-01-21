
#!/usr/bin/env python3

"""
Imports numbers from numbers_source.get_numbers() and prints whether each is Even or Odd.
"""

from numbers_source import get_numbers

def is_even(n: int) -> bool:
    return n % 2 == 0

if __name__ == "__main__":
    for n in get_numbers():
        label = "Even" if is_even(n) else "Odd"
        print(f"{n}: {label}")

