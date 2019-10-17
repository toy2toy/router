#!/usr/bin/env python3

class Color:
    RED="\033[91m"
    GREEN="\033[92m"
    YELLOW="\033[93m"
    PURPLE="\033[94m"
    RESET="\033[00m"

def print_colored(color:Color, *messages:str)->None:
    for msg in messages:
        print(f"{color} {msg} {Color.RESET}")

if __name__ == "__main__":
    print_colored(Color.GREEN, "Welcome to fun coding")
    print_colored(Color.YELLOW, "Demostrate print_colored", "thank you!", "hope you like the color")
