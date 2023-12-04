# name_args - Accepts any number of named arguments and prints them in the pattern key : value one at a time.
def name_args(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")

name_args(name='Esteban', age=21)

# all_true - Returns True if all the elements in an iterable are true.
def all_true(iterable):
    return all(iterable)

# one_true - Returns True if one of the elements in an iterable is true.
def one_true(iterable):
    return any(iterable)

# recursive_factorial - Uses recursion to find the factorial of an integer.
def recursive_factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * recursive_factorial(n - 1)

# recursive_deduplicate - Recursively removes all adjacent duplicate letters from a string.
def recursive_deduplicate(s):
    if len(s) == 0:
        return ""
    elif len(s) == 1:
        return s
    else:
        if s[0] == s[1]:
            return recursive_deduplicate(s[1:])
        else:
            return s[0] + recursive_deduplicate(s[1:])

# recursive_reverse - Uses recursion to reverse a string.
def recursive_reverse(s):
    if len(s) == 0:
        return ""
    else:
        return s[-1] + recursive_reverse(s[:-1])

# Example usage:
name_args(name='John', age=25, city='New York')
print(all_true([True, True, True]))
print(one_true([False, False, True, False]))
print(recursive_factorial(5))
print(recursive_deduplicate("AABBCCDD"))
print(recursive_reverse("hello"))