from collections.abc import Iterator,Iterable
list_test=[]
tuple_test=()
dict_test={}
set_test=set()

print(isinstance(list_test,Iterator))
print(isinstance(tuple_test,Iterator))
print(isinstance(dict_test,Iterator))
print(isinstance(set_test,Iterator))

print(isinstance(list_test,Iterable))
print(isinstance(tuple_test,Iterable))
print(isinstance(dict_test,Iterable))
print(isinstance(set_test,Iterable))