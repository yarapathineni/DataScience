#tuple
#Tuples are immutable sequences, typically used to store collections of heterogeneous data
#(such as the 2-tuples produced by the enumerate() built-in).
#Tuples are also used for cases where an immutable sequence of homogeneous data is needed
#(such as allowing storage in a set or dict instance).

########################

# defining the tuple

tuple1 =(1,2,3)
print(tuple1)
print(type(tuple1))

tuple2:tuple = (10,20,30,40)
print(tuple2)
print(tuple2[0])
print(tuple2[0:2])


''' 

accessing the elements is pretty much similar to list

(1, 2, 3)
<class 'tuple'>
(10, 20, 30, 40)
10
(10, 20)

'''


