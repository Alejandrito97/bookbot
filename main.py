book_path = "books/frankenstein.txt"

def main():

    def open_and_read(path):
        with open(path) as file:
            book_text = file.read()
            return book_text


    def character_count(text):
        
        characters_dictionary = {}
        letters = list(text)

        for letter in letters:
            if letter in characters_dictionary:
                characters_dictionary[letter] += 1
            else:
                characters_dictionary[letter] = 1

        return characters_dictionary 
           
    text_to_count = open_and_read(book_path).lower()
    
    characters = character_count(text_to_count)
    print(characters) 

main()