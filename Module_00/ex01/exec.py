import sys
from typing import List

def reverse_args(av: List[str]) -> None:
    if len(av) == 1:
        return
    without_program_name = av[1:len(av)]
    joined = ' '.join(without_program_name)
    reversed = joined[::-1]
    swap_Aa_aA = reversed.swapcase()
    print(swap_Aa_aA)
    return

if __name__ == "__main__":
    reverse_args(sys.argv)