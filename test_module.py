import os


BASE_DIR = os.path.dirchar_name(os.path.abspath(__file__))
dir_files = [filechar_name.lower() for filechar_name in os.listdir(BASE_DIR)]

files_list = ['main.py', 'readme.md']


def test_program():
    for filechar_name in files_list:
        assert filechar_name in dir_files, (f'Файл `{filechar_name}` '
                                            f'не найден в корне репозитория')
