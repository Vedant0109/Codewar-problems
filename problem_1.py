def sol():
  ''' If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.

Note: If the number is a multiple of both 3 and 5,: only count it once. '''
  l= [12,15,30,-5,90,11,16,0]
  add_l= []
  for number in l:
    if number%3==0 and number%5==0:
      add_l.append(number)
    else:
      pass
  sum= 0
  for numbers in add_l:
    sum+=numbers

  print(f"The sum of multiples of 3 and 5 is {sum}")
    