rows = 6                        #Pattern(1,121,12321,1234321,123454321)
for i in range(1, rows + 1):
    for j in range(1, i - 1):
        print(j, end=" ")
    for j in range(i - 1, 0, -1):
        print(j, end=" ")
    print()