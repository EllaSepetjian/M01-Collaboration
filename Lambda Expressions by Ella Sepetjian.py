# Ella Sepetjian
# SDEV 220
# 6/28/2022

# Square my_list
my_list = [5,4,3]
print(list(map(lambda num: num**2, my_list)))

# Sort list by the second number in the tuple and print
a = [(0, 2), (5, 2), (9, 9), (10, -1)]

a.sort(key=lambda x: x[1])
print(a)
