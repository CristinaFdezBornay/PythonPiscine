from sys import argv
from typing import List
from random import randint

def ft_none(words: List[str]) -> None:
    for word in words:
        yield word

def ft_shuffle(words: List[str]) -> None:
    shuffle_set = set()
    len_words = len(words)
    word = words[randint(0, len_words - 1)]
    for i in range(len_words):
        while word in shuffle_set:
            word = words[randint(0, len_words - 1)]
        yield word
        shuffle_set.add(word)

def ft_unique(words: List[str]) -> None:
    unique = set()
    for word in words:
        if word not in unique:
            yield word
        unique.add(word)

def ft_ordered(words: List[str]) -> None:
    words_ordered = words.sort()
    for word in words:
        yield word

def generator(text: str, sep: str = " ", option: str = None) -> None:
    """Option is an optional arg, sep is mandatory"""
    ft_options = {
        None      : ft_none,
        'shuffle' : ft_shuffle,
        'unique'  : ft_unique,
        'ordered' : ft_ordered
    }
    if not isinstance(text, str) or option not in ft_options.keys():
        print("ERROR")
        exit()
    words = text.split(sep)
    return ft_options[option](words)

if __name__ == "__main__":
    if len(argv) < 2:
        exit()
    for word in generator(argv[1], " "):
        print(word)