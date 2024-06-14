any = int(input('Enter your respective number to see hollow diamond: '))
n =any*2-1
for i in range(any):
    if i == 0: 
        print('A'.center(n))
        continue 
    abcd = chr(64+i) 
    print(f"{abcd}{' '*(2*i-1)}{abcd}".center(n))  
    print()
for i in range(0, any-1)[::-1]:
    if i == 0:
        print('A'.center(n))
        continue
    abcd = chr(64+i)
    print(f"{abcd}{' '*(2*i-1)}{abcd}".center(n))
    print()