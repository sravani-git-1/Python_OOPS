a = int(input("Enter a value: "))
b = int(input("Enter a value: "))
print("swap of a is: ", b)
print("swap of b is: ", a)

a = a ^ b
b = a ^ b
a = a ^ b
print("a= ", a)
print("b= ", b)