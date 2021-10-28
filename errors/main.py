# Do not modify these lines
import os

__winc_id__ = "534d85ea1ab14924a91f9eccf6f3f30d"
__human_name__ = "errors"


# Test your functions here to make sure the functionality remains the same.
def main():
    foo = list(range(10))
    print(
        get_item_from_list(foo, 9),
        get_item_from_list(foo, -1),
        get_item_from_list(foo, 10),
    )
    ...


"""Change the three functions below from Look Before You Leap (LBYL) to Easier
to Ask for Forgiveness than Permission (EAFP)"""


def add(x, y):
    try:
        return x + y
    except TypeError:
        return 0


def read_file(filename):
    try:
        return open(filename, "r").read()
    except FileNotFoundError:
        return ""


def get_item_from_list(l, index):
    try:
        return l[index]
    except:
        return None


if __name__ == "__main__":
    main()
