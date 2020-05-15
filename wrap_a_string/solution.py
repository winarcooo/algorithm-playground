from textwrap import wrap

def wrap_string(string, max_width):
  print(max_width)
  result = wrap(string, max_width)

  for i in result:
    print(i)

if __name__ == '__main__':
  wrap_string('aasdfasdfasdf', 3)