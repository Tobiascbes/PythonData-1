#!/usr/bin/env python3

def interleave(*lists):
    newList = []
    for lists in zip(*lists):
       newList.extend(lists)
    return newList

def main():
    print(interleave([1, 2, 3], [20, 30, 40], ['a', 'b', 'c']))
    

if __name__ == "__main__":
    main()
