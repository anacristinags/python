# We have two monkeys, a and b, and the parameters a_smile and b_smile indicate if each is smiling.
# We are in trouble if they are both smiling or if neither of them is smiling.
#  Return True if we are in trouble.

def smile(monkeyA, monkeyB):
    if monkeyA and monkeyB:
        return True
    elif not monkeyA and not monkeyB:
        return True
    else:
        return False
    
# testando código 
print(smile(True, True)) # rindo ao mesmo tempo (we are in trouble = true)
print(smile(False, False)) # nenhum está rindo (we are in trouble =  true)
print(smile(True, False)) # rindo em momentos diferente (we are in trouble = false)
print(smile(False, True)) # rindo em momentos diferente (we are in trouble = false)
    