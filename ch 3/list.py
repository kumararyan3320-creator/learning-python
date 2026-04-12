# fruits = ["apple", "mango", "cherry", "banana"] #create a list
# fruits[1]="pinapple"  #change the value of index 1
# print(fruits) #print the list
# print(type(fruits)) #print the type of the variable fruits
# print(len(fruits)) #print the length of the list


# fruits = ["apple", "mango", "cherry", "banana"]
# fruits[0]
# fruits[-2]
# print(fruits[0]) #access the first element of the list
# print(fruits[-2]) #access the second-to-last element of the list

# fruits = ["apple", "banana", "orange"]
# fruits[2] = "grape"
# print(fruits)

# # check if a items is in the list
# if "apple" in fruits:
#     print("Yes, apple is in the fruits list")
# if "kiwi" not in fruits:
#     print("No, kiwi is not in the fruits list")   

# list = [10, 20, 30, 40, 50]
# print(list[2])  #access the element at index 2
# print(list[-3]) #access the element at index -3 (third element from the end) negative indexing starts from the end of the list
# print(list[1:4]) #access the elements from index 1 to 3 (4 is not included) slicing


#index in list 
# print(fruits[1]) 
# print(fruits[-3]) 
# print(fruits[1:3]) 
# print(fruits[-3:-1]) 

# Add items to the end of the list
'''list = [10, 20, 30]
list.append(40) #append() is used to add an item to the end of the list
print(list)
list.insert(2,50) #insert() is used to add an item at a specific index in the list
print(list)
list.extend([60, 70]) #extend() is used to add all the items of a list to another list
print(list)'''

'''more_fruits = ["kiwi", "papaya"]
fruits.extend(more_fruits) #extend() is used to add all the items of a list to another list
print(fruits)
fruits.remove("banana")
print(fruits)'''


#remove items from the list
'''list = [10, 20, 30, 40]
list.remove(30) #remove() is used to remove the first occurrence of an item from the list
print(list)
list.pop(1) #pop() is used to remove an item at a specific index from the list and return the removed item
print(list)
list.pop() #pop() without an index removes the last item from the list
print(list)'''

# list = [10, 20, 30]
# list[1:3] = [40, 50] #replace the elements from index 1 to 2 with new values
# print(list)

#Change in items/updating items in the list
# fruits = ["apple", "mango", "cherry", "banana"]
# fruits[1] = "pineapple" #change the value of index 1
# print(fruits)
# fruits[1:3] = ["grape", "kiwi"] #replace the elements from index 1 to 2 with new values
# print(fruits)

#shorting the list
# fruits.sort() #sort() is used to sort the elements of the list in ascending order
# print(fruits)
# fruits.sort(reverse=True) #sort() with reverse=True is used to sort the elements of the list in descending order
# print(fruits)

#list comprehension
# list = [40, 20, 30, 10]
# new_list = [i for i in list if i > 20] #create a new list with elements greater than 20
# print(new_list)

# #or 

# for i in list:
#     if i > 20:
#         new_list.append(i) #append() is used to add an item to the end of the list
# print(new_list)

# new_fruits = [fruits for fruits in fruits if "a" in fruits] #create a new list with elements that contain the letter "a"
# print(new_fruits)

# #copying a list
# new_fruits = fruits.copy() #copy() is used to create a copy of the list
# print(new_fruits)
# new_fruits = fruits + new_fruits #concatenate two lists to create a new list
# print(new_fruits)

#Nested list
# fruits = ["apple", "mango", "cherry", "banana"]
# fruits.insert(2, ["kiwi", "papaya"]) #insert a nested list at index 2
# print(fruits)
# print(fruits[2][0]) #access the first element of the nested list at index 2

'''Given a list in Python and provided the index of the elements, write a program to swap the two elements in the list.
Examples:

Input:
List = [23, 65, 19, 90], idx1 = 0, idx2 = 2
Output:
[19, 65, 23, 90]

Input:
List = [1, 2, 3, 4, 5], idx1 = 1, idx2 = 4
Output:
[1, 5, 3, 4, 2]'''

# lst = [23, 65, 19, 90]
# idx1 = 0
# idx2 = 2

# lst[idx1], lst[idx2] = lst[idx2], lst[idx1]
# print(lst)


# list = [10, 20, 30]
# idx1 = 0 
# idx2 = 2
# list[0] = list[2]
# print(list)


list = ['m','o','n','k','e','y']
print('@'.join(list))

chars = ['m','o','n','k','e','y']
print("".join(chars))

# 0R

list = ['m','o','n','k','e','y']
print("".join(list))
