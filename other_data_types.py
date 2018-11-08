# Some other data types

# complex - complex numbers
complex_number = 1 + 2j
new_complex_number = complex(5, 5)  # complex(real part, imaginary part)
print(complex_number, new_complex_number)

# long - in Python2, doesn't exist in Python3

# bytes and bytearray - a sequence in the range <0,256)
# bytes - immutable, bytearray - mutable
bytes_sequence = b"abc"
new_bytes_sequence = bytes("This is an example", "utf-8")
print(bytes_sequence, new_bytes_sequence)

# tuple - similar to list but immutable
tuple_type = (1, 2, 3, "Mickey")
my_list = [2, 4, 6, 8]
new_touple_type = tuple(my_list)
print(tuple_type, new_touple_type)

# set and frozenset - unordered collection of objects, don't record element position, don't support indexing, slicing...
# set - mutable, can't b used as dictionary key and as an element of another set
# frozenset - immutable, can be used as dictionary key and as an element of another set
# Conversion list to set - you get rid of duplicates and order the list
set_type = (3, 2, 5, 8, 5)
new_set_type = set([3, 2, 1, 5, 4, 4, 1])  # This values will be ordered and without duplicates
print(set_type, new_set_type)
