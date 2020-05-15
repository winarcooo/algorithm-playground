def average(array):
  # your code goes here
  item = set(array)

  sum = 0
  for i in item:
    sum = sum + i

  avrg = sum / len(item)

  return avrg

    

if __name__ == '__main__':
  # n = int(input())
  # arr = list(map(int, input().split()))
  arr = [161,182, 161, 154, 176, 170, 167, 171, 170, 174]
  result = average(arr)
  print(result)