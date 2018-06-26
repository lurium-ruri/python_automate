#! python3
# backupToZip.py フォルダ全体を連番付きZIPファイルにコピーする
import os
import zipfile
from pathlib import Path


def backup_to_zip(folder):
    folder = Path(folder).absolute

    number = 1
    while True:
        zip_filename = Path(f'{folder}_{str(number)}.zip')
        if not Path(zip_filename).exists:
            break
        number = number + 1

    print(f'Creating{zip_filename}...')
    backup_zip = zipfile.ZipFile(zip_filename, 'w')

    # FIXME
    for foldername, subfolders, filenames in os.walk(folder):
        print(f'Adding files in {foldername}...')
        backup_zip.write(foldername)
        for filename in filenames:
            new_base = Path(f'{folder}_')
            if filename.startswith(new_base) and filename.endswith('.zip'):
                continue
            backup_zip.write(Path(foldername).joinpath(filename))
    backup_zip.close
    print('Done.')


def main():
    backup_to_zip('C:\\delicious')


if __name__ == '__main__':
    main()
