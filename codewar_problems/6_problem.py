def solution():
  '''Return the number (count) of vowels in the given string.

We will consider a, e, i, o, u as vowels for this Kata (but not y).

The input string will only consist of lower case letters and/or spaces.'''
  sentence= "Hello, How are you?"
  sentence= sentence.lower()

  counter_a= sentence.count("a")
  counter_e= sentence.count("e")
  counter_i= sentence.count("i")
  counter_o= sentence.count("o")
  counter_u= sentence.count("u")
  counter= counter_a+counter_e+counter_i+counter_o+counter_u
  return counter

print(solution())