def get_book_text(file):
    with open(file) as f:
        return f.read()

def word_counter(text):
    word_list = text.split()

    print(f"Found {len(word_list)} total words")

def main():
    book_path = 'books/frankenstein.txt'
    texts = get_book_text('books/frankenstein.txt')
    
    word_counter(texts)

if __name__ == '__main__':
    main()