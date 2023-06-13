# Program to reverse strings in between:
ls = "KrishnaMurthy"


middle_word = len(ls) // 2

ls1 = ls[0:middle_word]
ls2 = ls[middle_word:]
print(ls)
print(ls1)
print(ls2)
ls_rev = ls1[::-1] + ls2[::-1]

print(ls_rev)
