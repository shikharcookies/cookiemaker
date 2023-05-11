def concatenate_tuples(nested_tuples, new_tuple):
    if type(nested_tuples) == tuple:
        nested_tuples = (nested_tuples,)

    return nested_tuples + (new_tuple,)

# example usage
nested_tuples = ((1, 2), (3, 4))
new_tuple = (5, 6)

result = concatenate_tuples(nested_tuples, new_tuple)

# print the original nested tuples
print("Original nested tuples:", nested_tuples)

# print the result of concatenation
print("Result of concatenation:", result)
