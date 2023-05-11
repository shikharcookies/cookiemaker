def all_even(lst):
    for item in lst:
        if item % 2 != 0:
            return False
    return True

my_dict = {"Dic1": [6, 8, 10], "Dic2": [8, 10, 12, 16], "Dic3": [10, 16, 14, 6]}

for key in my_dict:
    if all_even(my_dict[key]):
        print(key, "values are all even")
    else:
        print(key, "values are not all even")
