# defining the list in python
#Lists are mutable sequences, typically used to store collections of homogeneous items (where the precise degree of similarity will vary by application).
list = [10,20,30,40,50]
print(list)
print(type(list))


list1 :list =([1,2,3,4,5])
print(list)

#accessing the list elements
print(2 in list1)
print(7 in list1)
print(7 not in list1)

print(list+list1)
print(list*list1)# erroes out and it is not possible
print(list1[0])
print(list1[2])
print(list1[7]) # errored out because of index is not there in the list.
print(list1[0:3])
print(list1[0:4:2]) # last parameter is step by 2.
print(len(list1))
print(min(list1))
print(max(list1))
print(list1.count(1))

#The out put is as follows.

'''
[10, 20, 30, 40, 50]
<class 'list'>
[10, 20, 30, 40, 50]
True
False
True
[10, 20, 30, 40, 50, 1, 2, 3, 4, 5]
Traceback (most recent call last):

  File "<ipython-input-1-fa5b3f7873b2>", line 15, in <module>
    print(list*list1)# erroes out and it is not possible

TypeError: can't multiply sequence by non-int of type 'list'




print(list1[0])
print(list1[2])
1
3

print(list1[0:3])
print(list1[0:4:2]) # last parameter is step by 2.
print(len(list1))
print(min(list1))
print(max(list1))
print(list1.count(1))
[1, 2, 3]
[1, 3]
5
1
5
1

'''


