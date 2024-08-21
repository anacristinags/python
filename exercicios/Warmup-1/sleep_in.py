# The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation.
# We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in. 
# (dormimos até mais tarde se NAO for dia de semana ou se estivermos de ferias)

def sleep_in(weekday, vacation): # definindo função 
  if not weekday or vacation:
    return True
  else:
    return False
  
# testando código 
print(sleep_in(False, False)) # não é dia de semana, mas não estamos de férias (sleep_in = true)
print(sleep_in(True, False)) # é dia de semana e não estamos de férias (sleep_in = false :( )
print(sleep_in(False, True)) # não é dia de semana e estamos de férias :) (sleep_in = true)
