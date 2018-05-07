#! python3
# pw.py -パスワード管理プログラム（脆弱性あり）
import sys
import pyperclip


def main():
    PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
                 'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
                 'luggage': '12345'}

    if len(sys.argv) < 2:
        print('使い方 python pw.py [アカウント名]')
        print('パスワードをクリップボードにコピーします')
        sys.exit()

    account = sys.argv[1]  # 最初のコマンドライン引数がアカウント名

    if account in PASSWORDS:
        pyperclip.copy(PASSWORDS[account])
        print(account+'のパスワードをクリップボードにコピーしました')
    else:
        print(account + 'というアカウント名はありません')


if __name__ == '__main__':
    main()
