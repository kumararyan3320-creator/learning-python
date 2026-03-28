fruits = ["apple", "mango", "cherry", "banana"] #create a list
# fruits[1]="pinapple"  #change the value of index 1
# print(fruits) #print the list
# print(type(fruits)) #print the type of the variable fruits
# print(len(fruits)) #print the length of the list



# fruits = ["apple", "banana", "orange"]
# fruits[2] = "grape"
# print(fruits)

#check if a items is in the list
'''if "apple" in fruits:
    print("Yes, apple is in the fruits list")
if "kiwi" not in fruits:
    print("No, kiwi is not in the fruits list")   ''' 

# list = [10, 20, 30, 40, 50]
# print(list[2])  #access the element at index 2
# print(list[-3]) #access the element at index -3 (third element from the end) negative indexing starts from the end of the list
# print(list[1:]) #access the elements from index 1 to 3 (4 is not included) slicing


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

more_fruits = ["kiwi", "papaya"]
fruits.extend(more_fruits) #extend() is used to add all the items of a list to another list
print(fruits)
fruits.remove("banana")
print(fruits)


#remove items from the list
list = [10, 20, 30, 40]
list.remove(30) #remove() is used to remove the first occurrence of an item from the list
print(list)
list.pop(1) #pop() is used to remove an item at a specific index from the list and return the removed item
print(list)
list.pop() #pop() without an index removes the last item from the list
print(list)

