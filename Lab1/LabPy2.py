# check if string is equal as to the reverse
# check the first character to the last character of the string and second to second last one 
# and so on …. If any character mismatches, the string wouldn’t be a palindrome.

def isPalindrome(str):
 
    # Run loop from 0 to len/2
    for i in range(0, int(len(str)/2)):
        if str[i] != str[len(str)-i-1]:
            return False
    return True

userInput = input("Enter word:")
print(isPalindrome(userInput))

