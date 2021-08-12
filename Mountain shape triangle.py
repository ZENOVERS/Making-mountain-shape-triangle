x = int(input())

for i in range(x):
    for j in range(1, 2*x):
        if x-i <= j <= x+i:
            print('*', end='')
            continue
        print(' ', end='')
    print()
