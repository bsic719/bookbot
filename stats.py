def word_count(text):
    word_list = text.split()

    print(f"Found {len(word_list)} total words")

def letter_count(text):
    l_count = {}

    for word in text:
        for l in word.lower():
            if l not in l_count:
                l_count[l] = 0
            l_count[l] += 1
    
    return l_count

def count_sort(letters):
    return letters['num']

def organized_letter_counter(text):
    letters = letter_count(text)
    organized_letters = []
    
    for letter, num in letters.items():
        organized_letters.append({'char': letter, 'num': num})
    organized_letters.sort(reverse=True, key=count_sort)
    
    return organized_letters

def print_letters(letters_sorted):
    for letter in letters_sorted:
        if letter['char'].isalpha():
            print(f"{letter['char']}: {letter['num']}")



