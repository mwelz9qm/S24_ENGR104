a = float(input("What is the coefficient a? "))
b = float(input("What is the coefficient b? "))
c = float(input("What is the coefficient c? "))
d = b * b - 4. * a * c

if d >= 0.0:
    print("Solutions are real")  # block 1
elif b == 0.0:
    print("Solutions are imaginary" )  # block 2
else:
    print("Solutions are complex")  # block 3
print("Finished")


