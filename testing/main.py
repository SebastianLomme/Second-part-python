def flatten(d, new_list):
    for val in d.values():
        if isinstance(val, dict):
            for sub_val in val.values():
                if isinstance(sub_val, dict):
                    flatten(sub_val, new_list)
                else:
                    new_list.append(sub_val)
        else:
            new_list.append(val)
    return new_list
        
def flatten_dict(dict):
    new_list = []
    return flatten(dict, new_list)



# print(flatten_dict({'a': 42, 'b': 3.14}))

# print(flatten({'a': {'inner_a': 42, 'inner_b': 350}, 'b': 3.14}))

print(flatten_dict({'a': {'inner_a': 42, 'inner_b': 350}, 'b': 3.14}))
print(flatten_dict({1:{2: 30, 3: 40, 4: 50}, 2: 20, 3: {2:50, 3: {1:10, 2:30}}}))