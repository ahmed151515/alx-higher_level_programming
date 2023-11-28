#!/usr/bin/python3
"""solve task"""


def text_indentation(text):
    """prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text (string): _description_

    Raises:
        TypeError: _description_
    """
    if type(text) != str:
        raise TypeError("text must be a string")
    # to if print 2 line thih convrt to True and next loop continue
    is_space = False
    for letter in text:
        if is_space:
            is_space = False
            continue
        print(letter,end="")
        if letter in '.?:':
            is_space = True
            print()
            print()


if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/5-text_indentation.txt')
