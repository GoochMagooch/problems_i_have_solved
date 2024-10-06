# a timer that counts down from 10 while only displaying the number that the loop is on

# set the current time with datetime and elapse 10 seconds, with each iterable printing after each second
import time
def timer(num):
    for i in range(num, 0, -datetime.tm_sec()):
        print(i)
    print("Blastoff!")

timer(10)

print(time.tm_sec)