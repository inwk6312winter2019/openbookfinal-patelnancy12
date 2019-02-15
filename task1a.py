# to complete task1 a of open book
import string

fout = open("Book1.txt",'r')
fout = fout.read()
words = fout.split("\n")

def unique_words():
  unique_words = []
  if words in fout:
    if words not in fout:
      unique_words[word] = 1
    else:
      unique_word[word] += 1

def count_the_article():
  str1 = []
  fout = open("Book1.txt",'r')
  r = fout.readlines()
  for line in r:
    str2 = line.lower().strip(string.punctuation + string.whitespace)
    str1 += str2
  total = {}
  for word in  str1:
    total[word] = total.get(word, 0) + 1
  words_t = len(str1)
  words_d = len(total.keys())
  print("Total Words : " + str(words_d))

print(count_the_article())
#unique_words()
