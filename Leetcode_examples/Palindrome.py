def isPalindrome(x):
    if x<0:
        return False
    return str(x)==str(x)[::-1]
print(isPalindrome(121))