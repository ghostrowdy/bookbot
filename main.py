from stats import count_characters, sort_character_dictionary, display_word_count, sort_on
import sys

def main():
    if len(sys.argv) < 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    count = count_characters(sys.argv[1])
    sorted_list = sort_character_dictionary(count)
    print('============ BOOKBOT ============')
    print(f'Analyzing book found at {sys.argv[1]}')
    print('----------- Word Count ----------')
    display_word_count(sys.argv[1])
    print('--------- Character Count -------')
    for i in sorted_list:
        if i['char'].isalpha():
            print(f'{i['char']}: {i['num']}')
    print('============= END ===============')

def get_book_text():
    with open('books/frankenstein.txt') as f:
        print(f.read())
        
main()
