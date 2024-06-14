def multiple(m,n):
   a = range(n, (m*n)+1,n)
   print(*a)
m = int(input('How many times: '))
n = int(input('Enter the number: '))
multiple(m,n)