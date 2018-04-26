def main():
    spam = ['apples', 'bananas', 'tofu', 'cats']
    print(get_array_str(spam))


def get_array_str(arr):
    ret_str = ''
    arr_last_idx = len(arr) - 1
    for i in range(arr_last_idx - 1):
        ret_str += arr[i] + ', '

    ret_str += 'and ' + arr[arr_last_idx]
    return ret_str


if __name__ == '__main__':
    main()
