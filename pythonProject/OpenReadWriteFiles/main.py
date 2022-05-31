# # optie 1
# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close()
#
# # optie 2
# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)


# mode="w" = write
# mode="a" = append
# if file is on desktop
with open("../../../../Users/Robby/Desktop/new_file.txt", mode="w") as file:
    file.write("\n New tefsdxt.")

# C:/Github/PycharmProjects/pythonProject/OpenReadWriteFiles/main.py