# -*- coding: utf-8 -*-
# Palabra Palindromo

def word_palindrome(word):
    reversed_letters = []

    for letter in word:
        reversed_letters.insert(0, letter)
    
    reversed_word = ''.join(reversed_letters)

    if reversed_word == word:
        return True
    return False

#other method
def isPalindrome(word):
    reversed_word = word[::-1]
    if reversed_word == word:
        return True
    return False


def run():
    word = str(input('Type word: ')).lower()
    #result = word_palindrome(word)
    result = isPalindrome(word)
    if result:
        print('The word {} is palindrome'.format(word))
    else:
        print('The word {} isnot palindrome'.format(word))

if __name__ == '__main__':
    run()