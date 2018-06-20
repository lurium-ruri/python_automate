#! python3
# mcb.pyw - クリップボードのテキストを保存・復元
# Usage:
# py.exe mcb.pyw save<keyword> - クリップボードをキーワードに紐づけて保存
# py.exe mcb.pyw <keyword> - キーワードに紐付けられたテキストをクリップボードにコピー
# py.exe mcb.pyw list - 全キーワードをクリップボードにコピー


import shelve
import sys

import pyperclip


def main():
    mcb_shelf = shelve.open('mcb')

    if len(sys.argv) == 3:
        # クリップボードの内容を保存
        if sys.argv[1].lower() == 'save':
            mcb_shelf[sys.argv[2]] = pyperclip.paste()
            print('save')

        # クリップボードの内容を削除
        if sys.argv[1].lower() == 'delete':
            del mcb_shelf[sys.argv[2]]
            print('delete')

    elif len(sys.argv) == 2:
        # キーワード一覧と、内容の読み込み
        if sys.argv[1].lower() == 'list':
            pyperclip.copy(str(list(mcb_shelf.keys())))
            print('list')
        elif sys.argv[1] in mcb_shelf:
            pyperclip.copy(mcb_shelf[sys.argv[1]])
            print('load')

    mcb_shelf.close()


if __name__ == '__main__':
    main()
