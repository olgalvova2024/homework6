my_dict={'Olga':1975,'Dasha':2001,'Danil':1999}
print('Dist: ',my_dict)
print('Existing value: ',my_dict['Danil'])
print('Non exsisting value: ',my_dict.get('Oleg','такого ключа нет'))
my_dict.update({'Svetlana':1974,'Andrey':1991})
print(my_dict)
del_name=my_dict.pop('Svetlana')
print('Deleted value: ',del_name)
print('Modified dictionary: ',my_dict)
# _______________________________________________________
my_self={'Olga','Dasha',10,11,13,True,False,True,14,13,11,6.8,6.9,7.7,6.8}
print('Set: ',my_self)
my_self.update({'Danil',1991})
my_self.discard(13)
print('Modified set: ',my_self)