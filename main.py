from stats import word_count, letter_count, organized_letter_counter, print_letters

def get_book_text(file):
    with open(file) as f:
        return f.read()

def main():
    book_path = 'books/frankenstein.txt'
    texts = get_book_text('books/frankenstein.txt')
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count(texts)} total words")
    print("--------- Character Count -------")
    print_letters(organized_letter_counter(texts))
    print("============= END ===============")

if __name__ == '__main__':
    main()