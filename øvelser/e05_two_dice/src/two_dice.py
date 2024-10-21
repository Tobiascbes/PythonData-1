#!/usr/bin/env python3

def main():
    diceOne = (1, 2, 3, 4, 5, 6)
    diceTwo = (1, 2, 3, 4, 5, 6)
    for i in diceOne:
        for j in diceTwo:
            if i + j ==5:
                print(f"({i},{j})")

if __name__ == "__main__":
    main()
