#!/usr/bin/python
import sys

#Python script that returns the roots of a quadratic equation
#of the form a*x^2 + b*x + c = 0
#Enter values for a, b, and c in the command line
#e.g. run: >python quadratic.py 1 2 -15
def main():
    a = sys.argv[1]
    b = sys.argv[2]
    c = sys.argv[3]
    num1 = 0
    num2 = 0
    num3 = 0
    while True:
        try:
            num1 = float(a)
            num2 = float(b)
            num3 = float(c)
            assert num1 != 0
            break
        except:    
            print("Please input only integers")
            a = input('Enter leading nonzero coefficient: ')
            b = input('Enter second coefficient: ')
            c = input('Enter constant: ')
    x1, x2 = find_roots(int(num1), int(num2), int(num3))
    print ("This is x1: ", x1)
    print ("This is x2: ", x2)


def find_roots(a,b,c):
    mid = b**2 - 4*a*c
    sqrt_mid = mid**(1/2)
    x1 = (-b + sqrt_mid)/(2*a)
    x2 = (-b - sqrt_mid)/(2*a)
    return x1, x2


if __name__=="__main__":
        main()
