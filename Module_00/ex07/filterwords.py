import sys
from typing import List
from string import punctuation

if __name__ == "__main__":
    try:
        if len(sys.argv) != 3:
            raise
        nbr_chr: int = int(sys.argv[2])
        words_list_unclean: List[str] = sys.argv[1].split(' ')
        words_list: List[str] = list(map(lambda word: word.strip(punctuation), words_list_unclean))
        filtered_words: List[str]  = [word for word in words_list if len(word) > nbr_chr]
        print(filtered_words)
    except:
        print('ERROR')
        exit()
