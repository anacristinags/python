# Given a string, return a new string where the first and last chars have been exchanged.
def front_back(str):
  if len(str) <=1:
    return str
  return str[-1] + str[1:-1] + str[0]

# testando 
print(front_back("aavj")) # java :)
print(front_back("nythop")) # python
print(front_back("code")) # eodc 