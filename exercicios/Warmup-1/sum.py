# Given two int values, return their sum. Unless the two values are the same,
# then return double their sum.

def sum(a, b):
  if a != b:
    return a+b
  else:
    return (a+b)*2
  
# testando 
print(sum(1,1)) # valores iguais, o dobro da soma (sum = 4)
print(sum(3,1)) # valores diferentes, soma (sum = 4)