def isPalindrome(x: int):
    str_x = str(x)
    reversed = str_x[::-1]
    if (str_x == reversed):
        return True
    return False


x = '123'
print(isPalindrome(x))
