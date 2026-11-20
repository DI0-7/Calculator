from Addition import add
from Subtraction import subtract
from Multiplication import mul
from Division import div

class Calculator:
    x = int(input("Enter 1st number: "))
    y = int(input("Enter 2nd number: "))
    print("[1] Addition")
    print("[2] Subtraction")
    print("[3] Multiplication")
    print("[4] Division")
    z=int(input("Choose operation: "))

    if z == 1:
        print(add(x,y))
    if z == 2:
        print(subtract(x,y))
    if z == 3:
        print(mul(x,y))
    if z == 1:
        print(div(x,y))