def collatz(num):
    if num % 2 == 0:
        return num // 2
    else:
        return 3 * num + 1

print('Enter a number: ')
num = int(input('> '))

while num != 1:
    num = collatz(num)
    print(num, end=' ')
