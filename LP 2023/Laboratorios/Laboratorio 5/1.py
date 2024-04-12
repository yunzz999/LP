def palindrome(s):
    if(s==s[::-1]):
        return True
    else:
        return False

def capicua (n):
    n=str(n)
    if(n==n[::-1]):
        return True
    else:
        return False

def digitos(s):
    for i in s:
        if not(i.isdigit()):
            return False
    return True

print(digitos("123"))