def prime(num):
     for i in range(2,num):
          if num % i == 0:
               break
     else:
          return True

list1 = list(range(2,50))
sum_Prime = 0

for i in list1:
     x = prime(i)
     if x is True:
          sum_Prime += i
print("Sum of prime::",sum_Prime)