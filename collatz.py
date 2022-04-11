import math

while True:
      num = int(input(": "))
      list = [num]
      while True:
            if num % 2 == 0:
                  num = math.floor(num / 2)
                  even = num
                  list.append(even)
            elif num % 2 != 0 :
                  num = math.floor(num * 3 + 1)
                  odd = num
                  list.append(odd)

            if num == 1:
                  print(list)
                  break