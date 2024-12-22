'''
    Geometry (Complex and Polar)
'''
import math as m
# import the classes
from Complex import Complex
from Polar import Polar
def get_a(self):
    """return first part of complex(absscissa) or polar number(radius)"""
    if isinstance(self,Complex):
        return self.x
    if isinstance(self,Polar):
        return self.r
    raise TypeError("The entered number is not of type complex or Polar")

def get_b(self):
    """return second part of complex(ordinate) or polar number(angle)"""
    if isinstance(self,Complex):
        return self.y
    if isinstance(self,Polar):
        return self.t
    raise TypeError("The entered number is not of type complex or Polar")

def modulus(comp:Complex):
    '''return modulus of the complex number'''
    j = get_a(comp)
    k = get_b(comp)
    return round(m.sqrt(j**2 + k**2),1)

def arg(comp:Complex):
    '''return arg (angle) of the complex number'''
    num = get_a(comp)
    denom = get_b(comp)
    return round(m.atan(num/denom),1)

def abscissa(pol:Polar):
    '''return abscissa of the polar point'''
    radius = get_a(pol)
    angle = get_b(pol)
    return round(radius*m.cos(angle),1)

def ordinate(pol:Polar):
    '''return ordinate of the polar point'''
    radius = get_a(pol)
    angle = get_b(pol)
    return round(radius*m.sin(angle),1)

def distance(z1_comp:Complex, z2_comp:Complex):
    '''distance between points'''
    z1_abscissa = get_a(z1_comp)
    z1_ordinate = get_b(z1_comp)
    z2_abscissa = get_a(z2_comp)
    z2_ordinate = get_b(z2_comp)
    return round(m.sqrt(((z1_abscissa-z2_abscissa)**2 + (z1_ordinate-z2_ordinate)**2)),1)

if __name__ == '__main__':
    # you can use this area of code to check all the functions manually
    # one example of using the functions has been shown
    # run this using "python3 main.py"
    a = Complex(4,2)
    b = Complex(2,2)
    z = a + b # uses the overloaded add
    print(f"Argument of a: {arg(a)} radian")
    print("Modulus of a",modulus(a))
    print("Modulus of b",modulus(b))
    print("z = ",z)
    print("Distance between a and b",distance(a, b))
    print("Modulus of z",modulus(z)) # you can call after you implement
    x = Polar(2,m.pi/3) # uses the overloaded power
    print("Square of x: ",x ** 2)
    print("abscissa of x",abscissa(x))
    print("abscissa of x",ordinate(x))
