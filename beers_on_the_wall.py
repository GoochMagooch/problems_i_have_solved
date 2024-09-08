i = 99
while i > 0:
    if i == 2:
        print(f"{i} bottles of beer on the wall, {i} bottles of beer")
        print(f"Take one down, pass it around, {i - 1} bottle of beer on the wall")
        i -= 1
        print(f"{i} bottle of beer on the wall, {i} bottle of beer")
        print(f"Take one down, pass it around, {i - 1} bottles of beer on the wall")
        break
    print(f"{i} bottles of beer on the wall, {i} bottles of beer")
    print(f"Take one down, pass it around, {i - 1} bottles of beer on the wall")
    i -= 1
print("No more bottles of beer on the wall, no more bottles of beeeeer")
