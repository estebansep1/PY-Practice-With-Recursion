# Write code for algorithm 5 below
def palindrome(str):
    if len(str) == 1 or len(str) == 0:
        return True
    else:
        return (str[0] == str[-1]) and palindrome(str[1: -1])
    
print(palindrome('racecar'))