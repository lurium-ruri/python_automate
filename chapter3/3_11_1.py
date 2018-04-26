def main():
    while True:
        try:
            num = int(input('数字を入力してね:'))
            break
        except KeyboardInterrupt:
            print("終了します")
        except ValueError:
            print("値が不正です")
        except Exception as e:
            print("不明なエラー")
            print(e)
    calc_num = num
    while True:
        calc_num = collatz(calc_num)
        print(calc_num)
        if calc_num == 1:
            break


def collatz(number):
    return int(number / 2) if number % 2 == 0 else int(3 * number + 1)


if __name__ == '__main__':
    main()
