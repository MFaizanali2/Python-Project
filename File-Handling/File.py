# file = open("data.txt", "w")
# file.write("This is Python\n")
# file.write("Python is versatile language\n")
# file.close()


# file = open("data.txt", "a")
# file.write("This is Python\n")
# file.write("Python is most comman language\n")
# file.close()



# file = open("data.txt", "r")
# content = file.read()
# print(content)
# file.close()

# with open("data.txt", "r") as file:
#     print(file.read())

name = input("Enter Your Name: ")
age = input("Enter Your Age: ")

with open("user.txt", "w") as file:
    file.write(name + "\n")
    file.write(age)
    
print("Save Succesfully!")