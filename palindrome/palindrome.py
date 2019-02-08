def ifPalindrome(inVar):
    revInvar = []
    for _ in range((len(inVar)-1), -1, -1):
        revInvar.append(inVar[_])
    if revInvar == inVar:
        return "Palindrome"
    else:
        return "Not a palindrome"

a = list(map(str, input("Enter a string : ")))
print(ifPalindrome(a))
