n = int(input("Enter the size of list:"))
list = []
for _ in range(n):
    num = int(input())
    list.append(num)

idx1 = int(input("Enter the index of first element:"))
idx2 = int(input("Enter the index of second element:"))

#swaping values of idx1 and idx2
temp = list[idx1]
list[idx1] = list[idx2]
list[idx2] = temp
print(list)