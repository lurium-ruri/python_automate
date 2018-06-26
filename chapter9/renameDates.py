#! python3
# renameDates.py - 米国式日付を欧州式に書き換える

import shutil
import os
import re


def main():
    date_pattern = re.compile(r"""~(.*?)
    ((0|1)?\d)-
    ((0|1|2|3)?\d)-
    (.*?)$
    """, re.VERBOSE)

    for amer_filename in os.listdir('.'):
        mo = date_pattern.search(amer_filename)

        if mo == None:
            continue

        before_part = mo.group(1)
        month_part = mo.group(2)
        day_part = mo.group(4)
        year_part = mo.group(6)
        after_part = mo.group(8)

        euro_filename = f'{before_part}{day_part}-{month_part}-{year_part}{after_part}'

        print(f'Renaming {amer_filename} to {euro_filename}')


if __name__ == '__main__':
    main()
