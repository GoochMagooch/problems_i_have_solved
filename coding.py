# SCROLL AND BE REMINDED OF HOW FAR YOU'VE COME
# THESE ARE PIECES OF CODE THAT YOU DID YOURSELF
# PIECES OF CODE THAT CAME FROM YOU THINKING AND SOLVING, WITH NEXT TO NO REFERENCE AND NO REFERENCE ON SOME

# Monday July 22, 2024
# prints a descending pyramid of hashes, using nested for loops
def pyramid():
    for i in range(5, 0, -1):
        for j in range(i):
            print('*', end='')
        print()

pyramid()

# Monday July 22, 2024
# counts down to 0 from n
def timer(n):
    if not n:
        return 0
    while n >= 0:
        print(n)
        n -= 1
    
timer(10)

# Monday July 22, 2024
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

def vowel_counter(string):
  vowel_count = 0
  for char in string:
    if char in vowels:
      vowel_count += 1
  return vowel_count

print(vowel_counter("random string that should print 7"))

# Friday August 23, 2024
# unsolved code that is meant to run through a series of string methods on a list of poems, authors and years, eventually creating a string for each
highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"
highlighted_poems_list = highlighted_poems.split(',')
print(highlighted_poems_list)

highlighted_poems_stripped = []
for poem in highlighted_poems_list:
  highlighted_poems_stripped.append(poem.strip())
print(highlighted_poems_stripped)

highlighted_poem_details = []
for item in highlighted_poems_stripped:
  highlighted_poem_details.append(item.split(':'))
print(highlighted_poem_details)

titles = []
poets = []
dates = []

for item in highlighted_poem_details:
  titles.append(item[0])
  poets.append(item[1])
  dates.append(item[2])

for item in highlighted_poem_details:
  print("The poem {} was published by {} in {}".format(titles, poets, dates))