def fizzbuzz (x):
    if x % 5 ==0 and x % 3 ==0:
        return "fizzbuzz"
    if x % 5 ==0:
        return 'Buzz'
    elif x%3 ==0:
        return 'Fizz'
    else:
        return x

print(fizzbuzz(15),fizzbuzz(12),fizzbuzz(10),fizzbuzz(4))

def pal (w):
    if w == w[::-1]:
        return True
    else: return False
print(pal('alah'),pal('ala'),pal('zovoz'))

def co (text):
    return len(text.split())
print(co('zooov z peremoga'))