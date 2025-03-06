import sys
from stats import nr_of_words, char_count, sort_list

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    
   
def main(path):


    # path = "books/frankenstein.txt"
    contents = get_book_text(path)
    length = nr_of_words(contents)
    char_counts = char_count(contents)
    sorted_list = sort_list(char_counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {length} total words")
    print("--------- Character Count -------")
    for dict in sorted_list:
        print(f"{dict["character"]}: {dict["count"]}")

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

main(sys.argv[1])