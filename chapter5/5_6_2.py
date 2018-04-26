from collections import Counter


def main():
    dragon_loot = [
        '金貨',
        '手裏剣',
        '金貨',
        '金貨',
        'ルビー'
    ]

    inv = {
        '金貨': 42,
        'ロープ': 1
    }
    inv = add_to_inventry(inv, dragon_loot)
    display_inventry(inv)


def display_inventry(inventory):
    print('持ち物リスト')
    item_total = 0
    for k, v in inventory.items():
        print(k + ' ' + str(v))
        item_total += v
    print('アイテム総数: ' + str(item_total))


def add_to_inventry(inventory, added_items):
    return dict(Counter(inventory) + Counter(added_items))


if __name__ == '__main__':
    main()
