'''
To find the given string is palindrome or not//
ex::abcba
    ama
    123454321
'''
def palin(string):
#x = input("Enter a string:: ")
    if len(string) % 2 != 0:
        print("Qualified to be palindrome ")
        if string.split(string[0]) == string.split(string[-1]):
            print("And yes!!It is palindrome")
        else:
            print("But,It is not a palindrome")
    else:
        print("Not a palindrome")
palin("ama")
palin("abcba")
palin("123454321")