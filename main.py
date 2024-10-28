
def print_report(word_count, char_dict):
  print("-- Begin character analysis report --")
  print(f"{word_count} words found in the document")
  print("\n")
  print_dict(char_dict)
  print("-- End report --")

def read_book(file_path):
  with open (file_path) as book:
    return book.read()

def count_words(contents):
  return len(contents.split())

def build_dict(contents):
  char_dict = {}
  for char in contents:
    c = char.lower();
    if not c.isalpha():
      continue

    if(c) in char_dict: 
      char_dict[c] +=1
    else:
      char_dict[c] = 1

  return char_dict

def print_dict(dict):
  for char, count in dict.items():
    print(f"The '{char}' character was found {count} times.")
  

def main():
  book = read_book("./books/frankenstein.txt")
  wc = count_words(book)
  dict = build_dict(book)
  print_report(wc, dict)

main()