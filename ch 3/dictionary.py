# A simple dictionary of names and phone numbers
phones = {
    "john": "555-1234",
    "Ria": "555-5678",
    "joy": "555-8765"
}
# print the dictionary
# print(phones) 

# checking type of the dictionary
# print(type(phones))

# lenth of the dictionary
# print(len(phones))

# access item of the dictionary
# print(phones["john"]) #accessing value of the dictionary using key
# print(phones.get("john")) #using get method
# print(phones.keys())#prints the keys of the dictionary
# (phones.values())#prints the values of the dictionary

# #update value of the dictionary
# phones["john"] = "555-4321" 
# print(phones)

# #add new item to the dictionary
# phones["joy"] = "555-6789"
# print(phones)
# phones["Ria"] = "555-9876"
# print(phones)

# more_phones = {
#     "Alice": "555-1111",
# }
# phones.update(more_phones)
# print(phones)

# #remove item from the dictionary
# phones.pop("john") #removes the item with the specified key
# print(phones)
# phones.popitem() #removes the last item added to the dictionary
# print(phones)
# phones.clear() #removes all items from the dictionary
# print(phones)

# print value of a dictionary
for x in phones:
    print(x) #prints the keys of the dictionary
    print(phones[x])#prints the values of the dictionary using the keys


# print element of a dictionary
    for x, y in phones.items():
        print(x, y) #prints the keys and values of the dictionary
    
#nested dictionary
phones = {
    "Area1": {
        "john": "555-1234",
        "Ria": "555-5678",
        "joy": "555-8765"
    },
    "Area2": {
        "Alice": "555-1111",
        "Bob": "555-2222",
        "cumins": "555-3333"
    }
}    
print(phones["Area1"]["john"]) #accessing value of the nested dictionary using keys
print(phones["Area2"]["Alice"]) #accessing value of the nested dictionary using keys



