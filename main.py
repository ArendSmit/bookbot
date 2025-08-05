#!/usr/bin/env python3

from sys import *
from stats import get_num_words
from stats import get_num_chars
from stats import get_sorted_num_chars

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents



def main2():
    get_num_words("books/frankenstein.txt")
    charDict = get_num_chars(get_book_text("books/frankenstein.txt"))
    for char in charDict:
        print(F"'{char}': {charDict[char]}")

def main():
    if len(argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        exit(1)
    fileName = argv[1]
    words = get_num_words(fileName)
    chars, wordNo = get_num_chars(words)
    #print (chars)
    #print (wordNo)
    print ("============ BOOKBOT ============")
    print (f"Analyzing book found at {fileName}...")
    print("----------- Word Count ----------")
    print(f"Found {wordNo} total words")
    print("--------- Character Count -------")
    charDict = get_sorted_num_chars(chars)
    for char in charDict:
        if char["char"].isalpha():
            print(F"{char["char"]}: {char["num"]}")
    print("============= END ===============")

main()
