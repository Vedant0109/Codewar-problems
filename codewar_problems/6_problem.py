def solution():
  '''Return the number (count) of vowels in the given string.

We will consider a, e, i, o, u as vowels for this Kata (but not y).

The input string will only consist of lower case letters and/or spaces.'''
  sentence= "Hello, How are you?"
  sentence= sentence.lower()
  vowels= ["a","e","i","o","u"]
  counter=0

  for letter in sentence:
    if letter in vowels:
      counter+=1
    else:
      pass
      
  print(counter)

solution()