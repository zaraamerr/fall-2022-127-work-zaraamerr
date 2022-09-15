# question 7

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

#test trials

print(is_even(10))
print(is_even(5))
print(is_even(1))
print(is_even(0))

#question 8

def is_odd(n):
  if is_even(n):
     return False
  else:
    return True

#test trials

print(is_odd(10))
print(is_odd(5))
print(is_odd(1))
print(is_odd(0))

#question 10 & 11

def is_rightangled(a, b, c):
    is_rightangled = False

    if a > b and a > c:
        is_rightangled = abs(b**2 + c**2 - a**2) < 0.001
    elif b > a and b > c:
        is_rightangled = abs(a**2 + c**2 - b**2) < 0.001
    else:
        is_rightangled = abs(a**2 + b**2 - c**2) < 0.001
    return is_rightangled


#test trials
print(is_rightangled(1.5, 2.0, 2.5))
print(is_rightangled(4.0, 8.0, 16.0))
print(is_rightangled(4.1, 8.2, 9.1678787077))
print(is_rightangled(4.1, 8.2, 9.16787))
print(is_rightangled(4.1, 8.2, 9.168))
print (is_rightangled(0.5, 0.4, 0.64031))