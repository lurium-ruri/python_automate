#! python3
# '7_18_1.py

import re


def main():
    password = input('パスワードを入力してください：')
    if test_password(password):
        print('test:OK')
    else:
        print('test:NG')


def test_password(text):
    test_length = re.match(re.compile(r'.{8,}'), text)

    if not test_length:
        print('8文字以上にしてください。')
        return False

    test_lower = re.search(re.compile(r'[a-z]'), text)
    if not test_lower:
        print('小文字英字を1文字以上含めてください。')
        return False

    test_upper = re.search(re.compile(r'[A-Z]'), text)
    if not test_upper:
        print('大文字英字を1文字以上含めてください。')
        return False

    test_number = re.search(re.compile(r'[0-9]'), text)
    if not test_number:
        print('数字を1文字以上含めてください。')
        return False
    return True


if __name__ == '__main__':
    main()
