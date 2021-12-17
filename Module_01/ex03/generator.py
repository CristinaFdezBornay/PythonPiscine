# from sys import argv, exit
from random import randint

def ft_none(words):
    """Function called by generator if option is none"""
    for word in words:
        yield word

def ft_shuffle(words):
    """Function called by generator if option = shuffle"""
    shuffle_set = set()
    len_words = len(words)
    word = words[randint(0, len_words - 1)]
    for _ in range(len_words):
        while word in shuffle_set:
            word = words[randint(0, len_words - 1)]
        yield word
        shuffle_set.add(word)

def ft_unique(words):
    """Function called by generator if option = unique"""
    unique = set()
    for word in words:
        if word not in unique:
            yield word
        unique.add(word)

def ft_ordered(words):
    """Function called by generator if option = ordered"""
    words.sort()
    for word in words:
        yield word

def generator(text, sep=" ", option=None):
    """Option is an optional arg, sep is mandatory"""
    ft_options = {
        None      : ft_none,
        'shuffle' : ft_shuffle,
        'unique'  : ft_unique,
        'ordered' : ft_ordered
    }
    if not isinstance(text, str) or option not in ft_options.keys() or not isinstance(sep,str):
        print("ERROR")
        return
    words = text.split(sep)
    return ft_options[option](words)
