# Given an int n, return the absolute difference between n and 21,
# except return double the absolute difference if n is over 21.

def diff21(n):
  if n < 21:
    return 21 - n
  else:
    return (n - 21) * 2
  
# testando 
print(diff21(20)) # menor que 21 (diferença de 1)
print(diff21(21)) # igual a 21 (diferença de 0 x 2 = 0)
print(diff21(50)) # maior que 21 (diferença de 29 x 2 = 58)