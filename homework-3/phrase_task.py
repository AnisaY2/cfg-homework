"""
Create required phrase.
----------------------

You are given a string of available characters and a string representing a word or a phrase that you need to generate.
Write a function that checks if you can generate required word/phrase using the characters provided.
If you can, then please return True, otherwise return False.

NOTES:
    You can only generate the phrase if the frequency of unique characters in the characters string is equal or greater
    than frequency in the document string.

FOR EXAMPLE:

    characters = "cbacba"
    phrase = "aabbccc"

    In this case you CANNOT create required phrase, because you are 1 character short!

IMPORTANT:
    The phrase you need to create can contain any characters including special characters, capital letter, numbers
    and spaces.

    You can always generate an empty string.

"""
from collections import Counter


def generate_phrase(characters, phrase):
    count_phrase = Counter(phrase)
    count_characters = Counter(characters)

    if len(characters) < len(phrase):
        return False                  # Phrase is too long
    else:
        for letter in count_phrase.keys():
            if letter not in count_characters.keys() or count_characters[letter] < count_phrase[letter]:
                return False          # Phrase contains character(s) not in the characters' string or that letters value in characters dict is less than how many the phrase needs
        return True
