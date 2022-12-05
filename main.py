book_path = "books/frankenstein.txt"

def main():

    def open_and_read(path):
        with open(path) as file:
            book_text = file.read()
            return book_text

    text = open_and_read(book_path)
    
    def count_words(text_to_count):
        words = text_to_count.split()
        return len(words)

    count = count_words(text)
    print(count)
           

main()