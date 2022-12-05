book_path = "books/frankenstein.txt"

def main():

    def open_and_read(path):
        with open(path) as file:
            book_text = file.read()
            return book_text

    text_to_print = open_and_read(book_path)
    print(text_to_print)        

main()