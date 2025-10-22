def main():
    display_word_amount()

def get_book_text():
    with open('books/frankenstein.txt') as f:
        print(f.read())

def display_word_amount():
    with open('books/frankenstein.txt') as f:
        word_list = f.read().split()
        print(f'Found {len(word_list)} total words')

main()
