from typing import Mapping


def greet(name):
    print(f"Good Morning , {name}")

# print(__name__)

if __name__== "__main__":   # allow only in this file no exporting...
    n=input("Enter a name\n")
    greet(n)

