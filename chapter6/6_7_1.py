def main():
    table_data = [['apples', 'oranges', 'cherries', 'banana'],
                  ['Alice', 'Bob', 'Carol', 'David'],
                  ['dogs', 'cats', 'moose', 'goose']]
    print_table(table_data)


def print_table(table):
    col_widths = [0] * len(table)  # 初期化
    for i in range(len(table)):
        tgt_row = table[i]
        col_widths[i] = len(max(tgt_row, key=len))

    for i in range(len(table[0])):
        row = ([row[i] for row in table])
        for j in range(len(row)):
            print(row[j].rjust(col_widths[j]), end=' ')
        print('')


if __name__ == '__main__':
    main()
