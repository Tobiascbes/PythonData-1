#!/usr/bin/env python3

def sum_equation(L):
    if not L:
        return "0 = 0"
    sumOf = sum(L)
    Eq = " + ".join(map(str, L))
    return f"{Eq} = {sumOf}"

def main():
    L = [1,5,7]
    print(sum_equation(L))

if __name__ == "__main__":
    main()
