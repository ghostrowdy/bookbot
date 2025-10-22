def main():
    get_book_text()

def get_book_text():
    with open('books/frankenstein.txt') as f:
        print(f.read())

main()
