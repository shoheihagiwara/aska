#!/bin/python3

def get_user_input():
  a = ""
  while True:
    try:
      a = a + input() + "\n"
    except EOFError:
      return a

def get_keyword_answer_map():
  map = dict()
  map[("test", "testing")] = "test successful"
  return map

def find_matching_answer(user_input, keyword_answer_map):
  answer_list = []

  for keywords,v in keyword_answer_map.items():
    everyword_present = True
    for keyword in keywords:
      if keyword not in user_input:
        everyword_present = False
    
    if everyword_present:
      answer_list.append(v)

  return answer_list

if __name__ == "__main__":

  user_input = get_user_input()

  keyword_answer_map = get_keyword_answer_map()

  answer = find_matching_answer(user_input, keyword_answer_map)

  print(answer)
