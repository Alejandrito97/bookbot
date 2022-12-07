book_path = "books/frankenstein.txt"

def main():
    
    def open_and_read(path):
        with open(path) as file:
            book_text = file.read()
            return book_text

    def count_words(text_book):
        words = text_book.split()
        return len(words)

    def character_count(text):        
        characters_dictionary = {}
        letters = list(text)

        for letter in letters:
            if letter in characters_dictionary:
                characters_dictionary[letter] += 1
            else:
                characters_dictionary[letter] = 1

        return characters_dictionary 
           
    def dict_to_list(dict_to_convert):
        
        new_list = []
        for key, val in dict_to_convert.items():
            if key.isalpha():
                new_list.append([key, val])

        new_list.sort(key= lambda a: a[1], reverse= True)
        return new_list
    
    text_to_count = open_and_read(book_path).lower()

    number_of_words = count_words(text_to_count)
    
    characters = character_count(text_to_count)

    sorted_list = dict_to_list(characters)
    
    print("--- Report of books/frankenstein.txt ---")
    print(f"{number_of_words} words found in the document")
    print(" ")
    for i in range(len(sorted_list)):
        print(f"The {sorted_list[i][0]} character was found {sorted_list[i][1]} times")
    print("--- End report ---")

main()