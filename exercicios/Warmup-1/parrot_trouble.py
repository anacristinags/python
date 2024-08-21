# We have a loud talking parrot. The "hour" parameter is the current hour time in the range 0..23.
# We are in trouble if the parrot is talking and the hour is before 7 or after 20. 
# Return True if we are in trouble.

def parrot_trouble(talking, hour):
  if talking and (hour < 7 or hour > 20):
    return True
  else: 
    return False 
  
# testando 
print(parrot_trouble(True, 7)) # está conversando, mas é depois das 7hrs (Are we in trouble? False)
print(parrot_trouble(True, 6)) # está conversando e é antes das 7hrs (Are we in trouble? True)
print(parrot_trouble(False, 23)) # não está conversando e é depois das 20hrs (Are we in trouble? False)
print(parrot_trouble(True, 22)) # está conversando e é depois das 20hrs (Are we in trouble? True)