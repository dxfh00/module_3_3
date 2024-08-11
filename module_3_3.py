def print_params(a, b, c):
    print(a, b, c)


values_list = (9, True, 'str')
values_dict = {'a': 11, 'b': 22, 'c': 33}
values_list2 = (54.32, 'str')
print_params(*values_list2, 42)
