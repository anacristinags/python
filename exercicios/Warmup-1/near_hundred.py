# Given an int n, return True if it is within 10 of 100 or 200. 
# Note: abs(num) computes the absolute value of a number.

def near_hundred(n):
    if ((abs(100 - n) <= 10) or (abs(200 - n) <= 10)):
        return True
    else:
        return False
    
# testando 
print(near_hundred(89)) # diferença é maior que 10 (False)
print(near_hundred(211)) # diferença é maior que 10 (False)
print(near_hundred(90)) # diferença é menor ou igual a 10 (True)
print(near_hundred(202)) # diferença é menor ou igual a 10 (True)