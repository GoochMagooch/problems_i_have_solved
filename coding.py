# prints a descending pyramid of hashes, using nested for loops
def pyramid():
    for i in range(5, 0, -1):
        for j in range(i):
            print('*', end='')
        print()

pyramid()

# counts down to 0 from n
def timer(n):
    if not n:
        return 0
    while n >= 0:
        print(n)
        n -= 1
    
timer(10)