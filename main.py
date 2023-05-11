my_list = [1,2,3,4,5]
my_list.append(10)
print("List after appending a value =" , my_list)
print("=====")
my_list.extend([6,11,23])
print("List after extending a list = ", my_list)
print("=====")
my_list.remove(3)
print("List after removing a value = ", my_list)

print(" ")
my_set = {1,2,6,5,7,11}
my_set.add(16)
print("Set after adding a value = ", my_set)

print(" ")
my_dict={"state":"WB", "Capital":"Kolkata"}
my_dict['Country']="India"
print("Dictionary after adding a new key-value pair=",my_dict)
my_dict['state']="West Bengal"
print("Dictionary after updating an existing key vlaue pair=",my_dict)
my_dict.pop('Capital')
print("Dictionary after popping out a key valuepair=",my_dict)
my_dict.clear()
print("After clearning the whole dictionary=",my_dict)