#! python3
# 8_10_2.py

import re
import sys
from pathlib import Path


def main():

    if len(sys.argv) < 2:
        sys.exit('''
        テキストファイルを指定してください
        ''')

    src_file = open(sys.argv[1], 'r', encoding='utf-8')
    src_data = src_file.read()
    src_file.close()

    # 置き換える文字列
    # FIXME グループ化しないと形容詞と形容動詞/動詞と形容動詞がうまく置き換えられない
    pattern = ['形容詞', '名詞', '形容動詞', '動詞', '副詞']

    for tgt in pattern:
        while True:
            replace_str = input(f'{tgt}を入力してください:')
            if replace_str != None:
                break
        src_data = src_data.replace(tgt, replace_str)

    print(src_data, end='')

    # テキストファイルに保存する
    dst_file = open(Path('replace.txt'), 'w', encoding='utf-8')
    dst_file.write(src_data)
    dst_file.close()


if __name__ == '__main__':
    main()
