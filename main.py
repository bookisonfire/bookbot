from stats import word_count
from stats import char_count
from stats import char_dict_to_list
import sys 



def get_book_text(book):
    with open(book) as f:
        return f.read()


#function to accept text from book as string and returns the number of words in the string  
def main():
     if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

     get_book_text(sys.argv[1])
     text = get_book_text(sys.argv[1])
     characters = char_count(text)
     count = char_dict_to_list(characters)
     word_count(text)
     print(f"Found {word_count(text)} total words")
     for items in count:
         if items["char"].isalpha():
             print(f"{items['char']}: {items['num']}")


main()