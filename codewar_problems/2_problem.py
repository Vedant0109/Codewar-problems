def sol() ->bool:
  '''An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

Example: (Input --> Output)

"Dermatoglyphics" --> true
"aba" --> false
"moOse" --> false (ignore letter case)
StringsFundamentals
Earn extra honor and gain'''
  word= "Hello"
  list_word=[]
  for letter in word:
    list_word.append(letter)
  set_word= set(list_word)
  leng= len(set_word)
  lenght= len(list_word)
  if len!=lenght:
    return False
  else:
    return True

print(sol())
