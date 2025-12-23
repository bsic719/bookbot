from stats import word_count, letter_count, organized_letter_counter, print_letters
import sys

def get_book_text(file):
    with open(file) as f:
        return f.read()

def main(file):
    book_path = file
    texts = get_book_text(book_path)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count(texts)} total words")
    print("--------- Character Count -------")
    print_letters(organized_letter_counter(texts))
    print("============= END ===============")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)

    main(sys.argv[1])