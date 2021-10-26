__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

from zipfile import ZipFile
import os

path = "/workspaces/test/Workspace/files/cache/"


def clean_cache():
    try:
        os.mkdir(path)
    except:
        list = os.listdir(path)
        for item in list:
            os.remove(f"{path}{item}")


# clean_cache()


def cache_zip(path_from, path_to):
    with ZipFile(path_from, "r") as zipObj:
        zipObj.extractall(path_to)


# cache_zip("/workspaces/test/Workspace/files/data.zip", path)


def cached_files():
    new_list = []
    list = os.listdir(path)
    for item in list:
        new_list.append(f"{path}{item}")
    return new_list


# print(cached_files())


def get_next_word(text, match):
    sl = text.split()
    all_is = [sl[i + 1] for i, word in enumerate(sl[:-1]) if word == match]
    return all_is[0]


def find_password(list):
    for item in list:
        file = open(item)
        read_file = file.read()
        if "password:" in read_file:
            password = get_next_word(read_file, "password:")
            return password


# print(find_password(cached_files()))
