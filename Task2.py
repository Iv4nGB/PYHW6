# # Задача 2. Дан список, вывести отдельно буквы и цифры.
# # a = ( "a", 'b', '2', '3' ,'c')
# # b = ( 'a' , 'b' , 'c')
# # c = ( '2', '3')

start_list = ['a', 'b', '2', '3', 'c']
print('a =', start_list)
print('b =', list(filter(lambda x: not x.isdigit(), start_list)))
print('c =', list(filter(lambda x: x.isdigit(), start_list)))