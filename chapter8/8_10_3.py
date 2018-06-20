#! python3
# -*- coding: utf-8 -*-
# 8_10_3.py

import os
import sys
import re


from pathlib import Path


def main():
    # if len(sys.argv) < 2:
    #     sys.exit('正規表現パターンを引数に指定してください')

    # pattern = re.compile(sys.argv[1])
    pattern = re.compile('a')

    p = Path('./chapter8')
    tgt_list = list(p.glob('*.text'))
    for filename in tgt_list:
        # テキストファイルを開く。文字コードはUTF-8とする。
        # シフトJISコードの場合は、encoding='shift_jis'としてください。
        txt_file = open(filename, 'r', encoding='utf-8')
        for i, line in enumerate(txt_file):
            mo = pattern.search(line)
            if mo:
                print(f'{filename} : {i + 1} : {line}', end='')
        txt_file.close()


if __name__ == '__main__':
    main()
