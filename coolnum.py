
nterms = 5


nterms = int(input("How many terms? "))


n1 = 0
n2 = 1
count = 0


if nterms <= 0:
   print(" Put in a positive number")
elif nterms == 1:
   print("Fibonacci sequence up to",nterms,":")
   print(n1)
else:
   print("Fibonacci sequence up to",nterms,":")
   while count < nterms:
       print(n1,end=' , ')
       nth = n1 + n2
      
       n1 = n2
       n2 = nth
       count += 1