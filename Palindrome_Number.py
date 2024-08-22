def isPalindrome(x: int) -> bool:
    string = str(x)
    string2 = ''
    for i in range(1, len(string)+1):
        string2 = string2 + string[-i]
    return string == string2


print(isPalindrome(173471))