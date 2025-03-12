# Listas, conceito e exemplos práticos
"""
A list contains items separated by commas and enclosed within square brackets [].lists are almost similar to arrays
in C. One difference is that all the items belonging to a list can be of different data type.
"""

list = [123,'abcd',10.2,'d'] #can be an array of any data type or single data type.
list1 = ['hello','world']
print(list) #will output whole list. [123,'abcd',10.2,'d']
print(list[0:2]) #will output first two element of list. [123,'abcd']
print(list1 * 2) #will gave list1 two times. ['hello','world','hello','world']
print(list + list1) #will gave concatenation of both the lists.
[123,'abcd',10.2,'d','hello','world']
