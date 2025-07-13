import sys
from stats import count_words
from stats import count_chars
from stats import sort_chars


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        bookfile = sys.argv[1]
        contents = get_book_text(bookfile)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {bookfile}...")
        print("----------- Word Count ----------")
        count_words(contents)
        print("--------- Character Count -------")
        char_dict = count_chars(contents)
        sort_chars(char_dict)
        print("============= END ===============")


main()