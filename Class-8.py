# file = open("student.html", "a")
# text = file.write("Easy \n Coding")
# print(text)

# type error
# try:
#     x = input("first nimber = ")
#     y = input("second number = ")
#     sum = x/y
#     print(sum)
# except TypeError:
#     print("Number Invalide")

# zero
try:
    x = int(input("Enter any number = "))
    div = 10/x
    print(div)
except (ZeroDivisionError, TypeError,ValueError):
    print("Number Invalid")
