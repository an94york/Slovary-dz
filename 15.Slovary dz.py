my_dict = {'Max' : 1999, 'Tim' : 2000, 'Olga' : 2003}
print(my_dict)
print(my_dict['Olga'])
print(my_dict.get('Zoy', 'без ошибки'))
my_dict.update({'Alex' : 1994, 'Ann' : 2006})
print(my_dict)
del my_dict['Alex']
print(my_dict)
v = my_dict.pop('Ann')
print(v)
print(my_dict)
my_set = {1,1,2,2,3,3,4,4,4,5,5,5}
print(my_set)
my_set = {1,1,2,2,3,3,4,4,4,5,5,5, False, 'Alise', (1,2,3)}
print(my_set)
my_set.discard(2)
print(my_set)
