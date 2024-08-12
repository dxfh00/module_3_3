def print_params(a=1, b='строка', c=True):
    print(a, b, c)


values_list = (9, True, 'str')
values_dict = {'a': 11, 'b': 22, 'c': 33}
values_list2 = (54.32, 'str')

print_params()
print_params(a='str', c=False)
print_params(b=25)
print_params(c=[1, 2, 3])

print_params(*values_list)
print_params(**values_dict)

print_params(*values_list2, 42)
