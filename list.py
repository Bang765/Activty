list = ['apple', 'banana', 'cherry', 'KIWI', 'mango']
print("length of list is :", len(list))
print("first element is : {list[0]}")
print("last element is : {list[-1]}")
list.append('orange')
print("length of list after append is :", len(list))
list.remove('banana')
print("length of list after remove is :", len(list))
list.sort()
print("sorted list is :", list)
list.pop(1)
print("length of list after pop is :", len(list))
list.reverse()
print("reversed list is :", list)

print ("multiplication on list :", list * 2)

list=list[:4]
print("sliced list is :", list)

list.clear()
print("length of list after clear is :", len(list))
