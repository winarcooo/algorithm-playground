import sys

def solution(baseWord, words):
    counter = 0
    for word in words:
        if set(baseWord).issubset(set(word)):
            counter += 1
    
    return counter


a = "love"
b = "vole svlove vloe asd wertwert svvolve"

def main():
  baseword = input().split()
  listword = input()

  print(solution(baseword, listword))

if __name__ == "__main__":
  main()