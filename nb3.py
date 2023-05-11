numbers = list(range(5,82,3))
strings = ["python","is","fun","!"]

def print_items(alist):
 for item in alist:
   print(item)

def print_items_bad(alist):
 length = len(alist)
 for index in range(length):
   print(alist[index])
  
def count_items(alist):
    c=0
    for item in alist:
       c=c+1
       return c

def count_odd_items(numlist):
 c=0
 for num in numlist:
   if num%2 == 1:
     c+=1
     return c
    
print_items(numbers)
print_items(strings)
print_items_bad(numbers)
print(count_items(numbers))
print(count_items(strings))
print(count_odd_items(numbers))