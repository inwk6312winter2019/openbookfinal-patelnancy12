# to complete task 1b of open book final exam
import string
 
def frequent_words():
  
  fout = open("Book1.txt",'r')
  fout = open("Book2.txt", 'r')
  fout = open("Book3.txt", 'r')
  r = fout.readlines()
  mydict = dict()
  for line in r:
    str2 = line.lower().strip(string.punctuation + string.whitespace)
    str1 += str2
    for item in str1:
      if item not in mydict:
        mydict[item] = 1
      else:
        mydict[item] += 1
 

print(frequent_words())

