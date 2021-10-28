__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

from zipfile import ZipFile
import os

currentPath = os.path.dirname(__file__)
path = os.path.join(currentPath, "cache")



def clean_cache():
    try:
        os.mkdir(path)
    except:
        list = os.listdir(path)
        for item in list:
            os.remove(os.path.join(path, item))


def cache_zip(path_from, path_to):
    with ZipFile(path_from, "r") as zipObj:
        zipObj.extractall(path_to)


def cached_files():
    new_list = []
    list = os.listdir(path)
    for item in list:
        new_list.append(os.path.join(path, item))
    return new_list


def get_next_word(text, match):
    list_text = text.split()
    password = [
        list_text[i + 1] for i, word in enumerate(list_text[:-1]) if match in word
    ]
    return password[0]


def find_password(list):
    for item in list:
        file = open(item)
        read_file = file.read()
        if "password:" in read_file:
            password = get_next_word(read_file, "password:")
            return password

