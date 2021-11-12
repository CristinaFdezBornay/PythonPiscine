import sys
from string import punctuation
from typing import Iterable

class string(str):
    def ispunct(c: Iterable[str]) -> bool:
        if c in punctuation:
            return True
        return False

def count(text: string) -> (int, int, int, int):
    isupper, islower, ispunct, isspace = 0, 0, 0, 0
    for c in text:
        isupper += string.isupper(c)
        islower += string.islower(c)
        ispunct += string.ispunct(c)
        isspace += string.isspace(c)
    return isupper, islower, ispunct, isspace

def text_analyzer(text: string = '', *arguments) -> None:
    '''
    This function counts the number of upper characters, lower characters,
    punctuation and spaces in a given text.
    '''
    if arguments:
        print('ERROR')
        return
    if text == '':
        text = input('What is the text to analyse?\n')
    isupper, islower, ispunct, isspace = count(text)
    print('The text contains {} characters:'.format(len(text)))
    print('- {} upper letters'.format(isupper))
    print('- {} lower letters'.format(islower))
    print('- {} punctuation marks'.format(ispunct))
    print('- {} spaces letters'.format(isspace))
    return
