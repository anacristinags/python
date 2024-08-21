# Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.

def makes10(a, b):
  if a == 10 or b == 10 or a+b == 10:
    return True
  else:
    return False 

# testando
print(makes10(1,9)) # apesar de serem diferentes a soma é 10 (True)
print(makes10(2,9)) # são diferentes e a soma não é 10 (False)
print(makes10(4,9)) # são diferentes e nem a soma é 10 (False)
print(makes10(10, 0)) # um deles é igual a 10 (True)
