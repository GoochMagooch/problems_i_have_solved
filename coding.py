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

# takes a list of integers, singles out the evens and returns a new list of even squared integers
def square_ints(lst):
    if not lst:
        return None
    return [i * i for i in lst if i % 2 == 0]
    
lst_of_ints = [1, 2, 3, 4, 5, 6]
print(square_ints(lst_of_ints))