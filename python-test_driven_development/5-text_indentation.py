#!/usr/bin/python3
"""this module contains a text indentation function"""


def text_indentation(text):
    """splits up a piece of text & adds new lines after special punctuation"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    new_text = ""
    space = False
    punc = [".", "?", ":"]
    for character in text:
        if character in punc:
            new_text += character + "\n\n"
            space = True
        elif character == " " and space is True:
            pass
        else:
            new_text += character
            space = False

    for line in new_text.split("\n"):
        print("".join(line.strip()))
