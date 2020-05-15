def arrange(sentence):
  words = sentence.replace('.', '').split()

  all_word = []
  for i in words:
    word_count = {
      'word': i,
      'count': len(i)
    }
    all_word.append(word_count)
  
  newList = sorted(all_word, key = lambda k: k['count'])

  result_list = []
  for word in newList:
    result_list.append(word['word'])

  result_string = " ".join(result_list) + "."

  return result_string.capitalize()


if __name__ == '__main__':
  test = 'The lines are printed in reverse order.'
  result = arrange(test)

  print(result)