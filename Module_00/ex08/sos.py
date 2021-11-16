import sys

morse_alphabet = {
    'a': '.-',
    'b': '-...',
    'c': '-.-.',
    'd': '-..',
    'e': '.',
    'f': '..-.',
    'g': '--.',
    'h': '....',
    'i': '..',
    'j': '.---',
    'k': '-.-',
    'l': '.-..',
    'm': '--',
    'n': '-.',
    'o': '---',
    'p': '.--.',
    'q': '--.-',
    'r': '.-.',
    's': '...',
    't': '-',
    'u': '..-',
    'v': '...-',
    'w': '.--',
    'x': '-..-',
    'y': '-.--',
    'z': '--..',
    '0': '-----',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.'
}

def parse_arguments():
    string = ""
    if len(sys.argv) == 1:
        sys.exit()
    elif len(sys.argv) >= 2:
        for arg in sys.argv:
            if arg == sys.argv[0]:
                continue
            arg = arg.split()
            for word in arg:
                if word.isalnum() == True:
                    string = string + ' ' + word
                else:
                    print("ERROR")
                    sys.exit()
    return string.strip()

def translate_to_morse(string):
    ret = ""
    for char in string:
        if char == ' ':
            ret = ret + '/'
        else:
            ret = ret + morse_alphabet[char.lower()]
        ret = ret + ' '
    return ret.strip()

if __name__=='__main__':
    string = parse_arguments()
    print(translate_to_morse(string))