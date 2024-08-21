# Given a string, return a new string where "not " has been added to the front. 
# However, if the string already begins with "not", return the string unchanged.

def not_string(str):
  if str[:3] == "not":
    return str
  else:
    return "not " + str
  
# testando
print(not_string("x")) # not x
print(not_string("is not")) # not is not 
print(not_string("not bad")) # not bad
print(not_string("bad")) # not bad