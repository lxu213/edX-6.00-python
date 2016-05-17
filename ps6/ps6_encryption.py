# 6.00x Problem Set 6
#
# Part 1 - HAIL CAESAR!
# https://github.com/simaofreitas/edx-mitx-6.00/blob/master/ProblemSet5/ps5_encryption.py
# http://ameenzhao.blogspot.com/2014/10/mitx-6001x-python-notes-caesar-cipher.html

import string
import random

WORDLIST_FILENAME = "words.txt"


# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    inFile = open(WORDLIST_FILENAME, 'r')
    wordList = inFile.read().split()
    print "  ", len(wordList), "words loaded."
    return wordList


def isWord(wordList, word):
    """
    Determines if word is a valid word.

    wordList: list of words in the dictionary.
    word: a possible word.
    returns True if word is in wordList.

    Example:
    >>> isWord(wordList, 'bat') returns
    True
    >>> isWord(wordList, 'asdf') returns
    False
    """
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\\:;'<>?,./\"")
    return word in wordList


def randomWord(wordList):
    """
    Returns a random word.

    wordList: list of words  
    returns: a word from wordList at random
    """
    return random.choice(wordList)


def randomString(wordList, n):
    """
    Returns a string containing n random words from wordList

    wordList: list of words
    returns: a string of random words separated by spaces.
    """
    return " ".join([randomWord(wordList) for _ in range(n)])


def randomScrambled(wordList, n):
    """
    Generates a test string by generating an n-word random string
    and encrypting it with a sequence of random shifts.

    wordList: list of words
    n: number of random words to generate and scamble
    returns: a scrambled string of n random words

    NOTE:
    This function will ONLY work once you have completed your
    implementation of applyShifts!
    """
    s = randomString(wordList, n) + " "
    shifts = [(i, random.randint(0, 25)) for i in range(len(s)) if s[i - 1] == ' ']
    return applyShifts(s, shifts)[:-1]


def getStoryString():
    """
    Returns a story in encrypted text.
    """
    return open("story.txt", "r").read()


# (end of helper code)
# -----------------------------------


#
# Problem 1: Encryption
#
def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers and spaces.

    shift: 0 <= int < 26
    returns: dict
    """
    lower = 2*string.ascii_lowercase
    upper = 2*string.ascii_uppercase
    new_alphabet = {}

    for i in range(26):
        new_alphabet[lower[i]] = lower[i+shift]
    for i in range(26):
        new_alphabet[upper[i]] = upper[i+shift]

    return new_alphabet


def applyCoder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text
    """
    coder_result = ""

    for letter in text:
        if letter not in string.ascii_lowercase and letter not in string.ascii_uppercase:
            coder_result += letter
        else:
            coder_result += coder[letter]
    print coder_result

def applyShift(text, shift):
    """
    Given a text, returns a new text Caesar shifted by the given shift
    offset. Lower case letters should remain lower case, upper case
    letters should remain upper case, and all other punctuation should
    stay as it is.

    text: string to apply the shift to
    shift: amount to shift the text (0 <= int < 26)
    returns: text after being shifted by specified amount.
    """

    return applyCoder(text, buildCoder(shift))

for i in range(26):
    print i
    print applyShift('lvygtylc', i)
#
# Problem 2: Decryption
#
def findBestShift(wordList, text):
    """
    Finds a shift key that can decrypt the encoded text.

    text: string
    returns: 0 <= int < 26
    """

    word_dict = {}
    wordList = loadWords()

    # test all possible shifts
    for i in range(26):
        real_words = 0
        text_list = string.split(applyShift(text, i))
        for word in text_list:
            if isWord(wordList, word):
                real_words += 1
        word_dict[i] = real_words
    return max(word_dict, key = word_dict.get)

def decryptStory():
    """
    Using the methods you created in this problem set,
    decrypt the story given by the function getStoryString().
    Use the functions getStoryString and loadWords to get the
    raw data you need.

    returns: string - story in plain text
    """

    story = getStoryString()
    print applyShift(story, findBestShift(loadWords(), story))

# Build data structures used for entire session and run encryption
#


# if __name__ == '__main__':
    # To test findBestShift:
    # wordList = loadWords()
    # s = applyShift('Hello, world!', 8)
    # bestShift = findBestShift(wordList, s)
    # assert applyShift(s, bestShift) == 'Hello, world!'
    # decryptStory()