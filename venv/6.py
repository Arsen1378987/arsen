
def is_prime(num):
    result = True;
    if num % 2 == 1:
        result  = True
    else:
        result = False
    return result

print(is_prime(0))
print(is_prime(1))
print(is_prime(10))
print(is_prime(1000))
print(is_prime(7))