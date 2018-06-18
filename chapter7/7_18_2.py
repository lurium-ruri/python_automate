#! python3
# '7_18_2.py

import re


def main():
    text = '  あ  '
    print(my_strip(text))

    text = 'XXXaXXXXaX  あ  XaXXXXaXXX'
    print(my_strip(text, 'XXXaX'))
    


def my_strip(text, *character):
    if character:
        char = character[0]
        l_regex = re.compile(fr'^({char})*')
        r_regex = re.compile(fr'({char})*$')
    else:
        l_regex = re.compile(r'^\s*')
        r_regex = re.compile(r'\s*$')
    text = l_regex.sub('', text)
    text = r_regex.sub('', text)
    return text


if __name__ == '__main__':
    main()
