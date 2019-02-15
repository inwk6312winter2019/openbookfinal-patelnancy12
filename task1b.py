# to complete task 1b of open book final exam
import string
import colletions
import sys
 
def frequent_words():
  str1 = []
  fout = open("Book1.txt",'r')
  fout = open("Book2.txt", 'r')
  fout = open("Book3.txt", 'r')

  r = fout.read().lower()
  words = collections.counter(r.split())
  print(words)



print(frequent_words())

