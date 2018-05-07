#! python3
# bulletPointAdder.py
# 点を打って、Wikipediaの箇条書きにする

import pyperclip


def main():
    text = pyperclip.paste()

    lines = text.split('\n')
    for i in range(len(lines)):  # "lines"リストの各要素をループする
        lines[i] = '* ' + lines[i]  # "lines"の要素に"* "を追加する
    text = '\n'.join(lines)

    pyperclip.copy(text)


if __name__ == '__main__':
    main()
