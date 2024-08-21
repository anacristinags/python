#  Given 2 int values, return True if one is negative and one is positive.
# Except if the parameter "negative" is True, then return True only if both are negative.

def pos_neg(a, b, negative):
  if not negative:
    if (a<0 and b>0) or (a>0 and b<0):
      return True
    else:
      return False
  if negative:
    if a<0 and b<0:
      return True
    else:
      return False
    
# testando
print(pos_neg(-1,-1, True)) # ambos são negativos e é True (True)
print(pos_neg(3,-1, True)) # um e positivo, outro é negativo e é True (False)
print(pos_neg(-4, 1, False)) # um é negativo, outro positivo e é False (True)