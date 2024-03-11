"""
Напишите код, который запускается из командной строки и получает на вход
путь до директории на ПК.
Соберите информацию о содержимом в виде объектов namedtuple.
Каждый объект хранит:
○ имя файла без расширения или название каталога,
○ расширение, если это файл,
○ флаг каталога,
○ название родительского каталога.
В процессе сбора сохраните данные в текстовый файл используя
логирование
"""
import os
from collections import namedtuple
import logging
import argparse

parser = argparse.ArgumentParser(description='Введите путь до директории')
parser.add_argument('-path', type=str, default='C:/Users')
args = parser.parse_args()

# path_main = 'C:/Users/user/PycharmProjects/pythonImSm/seminar7'


def directory_contents(path):
    DirectoryContents = namedtuple('DirectoryContents', ['name_file', 'ext_file', 'flag_dir',
                                                         'main_dir'],
                                   defaults=['Нет файлов', '', False, 'Нет директории'])

    main_dir = path[:path.rfind('/')]
    list_dir = os.listdir(path)
    logging.basicConfig(filename='dir_con.log', filemode='a', encoding='utf-8', level=logging.INFO)
    logger = logging.getLogger(__name__)

    for item in list_dir:
        if '.' in item:
            name_file = item[:item.rfind('.')]
            ext_file = item[item.find('.') + 1:]
            dc = DirectoryContents(name_file=name_file, ext_file=ext_file, main_dir=main_dir)
        else:
            dc = DirectoryContents(name_file=item, flag_dir=True, main_dir=main_dir)

        logger.info(f'{dc}')


directory_contents(f'{args.path}')
# directory_contents(path_main)