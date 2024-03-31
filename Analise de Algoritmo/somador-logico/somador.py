import math

def somador(a,b):
    soma = a ^b
    carry = a&b
    print(f"soma:{soma}")
    print(f"carry:{carry}")


somador(3,7)