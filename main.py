book_path = "books/frankenstein.txt"

def main():
  with open(book_path) as f:
      file_contents = f.read()

  total_words = count_words(file_contents)
  
  letters_dict = count_letters(file_contents)

  print_report(letters_dict, total_words)


def count_words(source):
    list_of_words = source.split()
    return len(list_of_words)

def count_letters(source):
  result = {}
  valid_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

  for letter in source:
      lower_case = letter.lower()
      if lower_case not in valid_letters:
        continue

      if lower_case not in result:
        result[lower_case] = 1
      else:
        result[lower_case] += 1
    
  return result

def print_report(source, total_words):

  sorted_dict = dict(sorted(source.items(), key=lambda item: item[1], reverse=True))
  
  print(f"--- Begin report of {book_path} ---")
  print(f"{total_words} words found in document")
  for letter, count in sorted_dict.items():
    print(f"The '{letter}' character was found {count} times")

main()