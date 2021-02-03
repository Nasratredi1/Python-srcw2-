# so we get from this that if there is sth wrong happen you must give a good input to user.
import sys

try:
    x= int(input("x: "))
    y= int(input("y: "))
except  ValueError:
    print("Error: Invalid input.")# if you write text inplace of int num then they print this value to you

try:
    result = x / y
    
except  ZeroDivisionError: # if exception happen print the below msg.
    print("Eror: cannot divide by 0.")
    sys.exit(1)  # then finish the program

print(f"{x} / {y} = {result}")

# so if i divide 5 into 0 then there is a exception happen so for removing this we have to give msg to user to know what is the exception .


