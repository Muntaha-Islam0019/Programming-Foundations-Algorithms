def gcd(a, b):

    r = None
    while True:
        r = a % b
        if r == 0:
            break
        a, b = b, r

    return b


print(gcd(60, 96))
print(gcd(20, 8))
