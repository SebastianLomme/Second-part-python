
from main import flatten_dict


def test_flatten_dict_is_list():
    assert isinstance(flatten_dict({'a': 42, 'b': 3.14}), list)  

def test_flatten_dict_1():
    assert flatten_dict({'a': 42, 'b': 3.14}) == [42, 3.14]

def test_flatten_dict_2():
    assert flatten_dict({'a': [42, 350], 'b': 3.14}) == [[42, 350], 3.14]

def test_flatten():
    assert flatten_dict({'a': {'inner_a': 42, 'inner_b': 350}, 'b': 3.14}) == [42, 350, 3.14]

def test_flatten_1():
    assert flatten_dict({1:{2: 30, 3: 40, 4: 50}, 2: 20, 3: {2:50, 3: {1:10, 2:30}}})  == [30, 40, 50, 20, 50, 10, 30]