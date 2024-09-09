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

word = "bottles"
for beer_num in range(99, 0, -1): 
    print(beer_num, word, "of beer on the wall.")
    print(beer_num, word, "of beer.")
    print("Take one down.")
    print("Pass it around.")

    if beer_num ==1:
        print("No more bottles of beer on the wall.")
        break
    else:
        new_num = beer_num - 1
        if new_num == 1:
            word = "bottle"
        print(new_num, word, "of beer on the wall.")
 
    print()