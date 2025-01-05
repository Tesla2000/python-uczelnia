from collections.abc import Iterable
from collections.abc import Sequence
from typing import SupportsIndex
from typing import Union
# source codes without imports

def primes(n: SupportsIndex):
  primes = []
  for number in range(2, n):
    if all(number % prime != 0 for prime in primes):
      primes.append(number)
  return primes

def prime_factors(n: Union[float, int]):
  result = []
  for divider in range(2, math.ceil(math.sqrt(n))):
    power = 0
    while (n % divider == 0):
      power += 1
      n = n // divider
    if (power > 0):
      result.append((divider, power))

  return result

def fraczero(n: Union[float, int]):
  zeros = 0
  while n > 0:
    n //= 5
    zeros += n
  return zeros

def rand_stuff(nums: SupportsIndex, start, end):
  numbers = [int(random.uniform(start, end)) for i in range(nums)]
  print(numbers)
  print(reduce(lambda prev, curr: prev + curr/len(numbers), numbers, 0))
  print(min(numbers), max(numbers))
  print(sorted(numbers)[1], sorted(numbers)[-2])
  print(len([n for n in numbers if n % 2 == 0]))

def matcher(strings: Iterable[Sequence], pattern: Iterable):
  dictionary = {i: c for i, c in enumerate(pattern) if c != "*"}
  return [s for s in strings if all(s[i] == c for i, c in dictionary.items())]

def rzymToArabNotException(rzymString: Iterable): #pdk xD
  values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
  arab = 0
  last = 0
  for c in rzymString:
    if values[c] > last:
      arab -= last
    else:
      arab += last
    last = values[c]
  return arab + last

def calc():
  x = input('Calc: ')
  print(eval(x))

def plotter():
  height = 24
  width = 80

  f = input('Function to plot: ')
  x0 = eval(input('From: '))
  x1 = eval(input('To: '))

  points = [x0 - i/width * (x0 - x1) for i in range(width)]
  vals = [eval(f) for x in points]
  yMax = max(vals)
  yMin = min(vals)

  for row in range(height):
    for i, column in enumerate(points):
      if row == round((yMax - vals[i])/(yMax - yMin) * height):
        print('*', end='')
      elif row == round(yMax / (yMax - yMin) * height):
        print('-', end='')
      elif i == round(x0 / (x0 - x1) * width):
        print('|', end='')
      else:
        print(' ', end='')
    print()
