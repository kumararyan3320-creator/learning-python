#creating a set
names = {"Alice", "Bob", "Charlie", "David"}
# print(names)
# #check lenghth of sets 
# print(len(names)) #print the length of the set
# #check data type of set
# print(type(names)) #print the type of the variable names

# # sets are unordered, so we cannot access elements using index

# #accessing elements of a set
# for x in names:
#     print(x)

# #check if an item exists in the set
# if "Alice" in names:
#     print("Yes, Alice is in the names set")

# add elements to a set
# names.add("Alice") #add() is used to add an item to the set but duplicate value cannot be added to the set
# print(names)
# #add another sequence of items to the set
# names_list = ["Eve", "Frank"]
# names.update(names_list) #update() is used to add all the items of a list to a set
# print(names)
# for removing items from the set
# names.remove("Bob") #remove() is used to remove an item from the set but it raises a KeyError if the item does not exist in the set
# print(names)
# names.remove("harry") #if we try to remove an item that does not exist in the set, it will raise a KeyError
# print(names)
# names.discard("harry") #discard() is used to remove an item from the set but it does not raise an error if the item does not exist in the set
# print(names)

#joining 2 sets
set1 = {"Alice", "Bob", "Charlie"}
set2 = {"David", "Eve", "Frank"}
print(set2,set1)

set3 = set1.union(set2) #union() is used to join two sets
print(set3)

# OR

set1.update(set2) #update() is used to add all the items of a set to another set
print(set1)

#keep only duplicates while joining two sets
set1.intersection_update(set2)#intersection_update() is used to keep only the items that are present in both sets
print(set1)

#keep all but not duplicates while joining two sets
set1.symmetric_difference_update(set2) #symmetric_difference_update() is used to keep all the items that are not present in both sets
print(set1)
