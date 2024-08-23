# SCROLL AND BE REMINDED OF HOW FAR YOU'VE COME
# THESE ARE PIECES OF CODE THAT YOU DID YOURSELF
# PIECES OF CODE THAT CAME FROM YOU THINKING AND SOLVING, WITH NEXT TO NO REFERENCE AND NO REFERENCE ON SOME

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

# Sunday August 18, 2024
# appends the sum of the last 2 integers in a list, three times, using a for loop
def append_sum(my_list):
  if not my_list:
    return 0
  for i in range(3):
    my_list.append(my_list[-1] + my_list[-2])
  return my_list

print(append_sum([1, 1, 2]))

# Monday August 19, 2024
# prints 'Oi Mate!' 10 times
def oi_mate():
  print("Oi Mate!")

i = 1
while i <= 10:
  oi_mate()
  i += 1

# Tuesday August 20, 2024
# prints the first 3 multiples of `num` and then returns the third multiple
def first_three_multiples(num):
  count = 1
  i = 0
  while count <= 3:
    i + num
    count += 1
    i += num
    print(i)
  count_two = 1
  j = 0
  while count_two <= 3:
    num + num
    count_two += 1
    j += num
  return j

first_three_multiples(10)
first_three_multiples(7)

# Thursday August 22, 2024
# counts the number of words in a string that begin with a capital, or lowercase M
my_sentence = "My gosh, what a beautiful Monday morning this is."

def m_word_count(string):
  word_list = string.split()
  m_words = 0
  for word in word_list:
    if 'm' in word[0] or 'M' in word[0]:
      m_words += 1
  return m_words

print(m_word_count(my_sentence))

# Friday August 23, 2024
# iterates through a string and returns the number of vowels
vowels = ["a", "e", "i", "o", "u"]

# Write your function here
def vowel_counter(string):
  vowel_count = 0
  for char in string:
    if char in vowels:
      vowel_count += 1
  return vowel_count

print(vowel_counter("random string that should print 7"))