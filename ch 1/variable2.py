#string
name = "Aryan"
 
#integer
roll_number = 24

#flooting number
percentage = 96

#boolean number
is_student = True 

# FLAG
show_old_value = True 
show_updated_value = False

#OLD VALUE
if show_old_value:
    print(name, roll_number, percentage, is_student)
    print("my name is", name, "and my roll number is", roll_number)
    print("i score", percentage, "% in final exam. i am a student is", is_student)

#UPDATE
percentage = percentage - 5.6

# ---- UPDATED VALUE ----
if show_updated_value:
 print("my name is", name, "and my roll number is", roll_number)
 print("i score", percentage, "% in final exam. i am a student is", is_student)

#seprator
print(name, roll_number, percentage, is_student, sep="-")
x = 1 
y = 2
z = 3 
print(x,y,z,sep="->")

