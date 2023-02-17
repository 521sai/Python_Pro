def outer_function(x):
    def inner_function(y):
        return y+x
    return inner_function
my_function = outer_function(2)
print(my_function(3))