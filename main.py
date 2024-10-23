def main():

    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_words_in_book(text)
    char_dict = count_chars(text)
    chars_sorted_list = chars_dict_to_sorted_list(char_dict)


    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document\n")
    
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The {item["char"]} character was found {item["num"]} times")
    
    print("--- End report ---")


def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words_in_book(text):
    words = text.split()
    return len(words)
        
    return word_count

def count_chars(text):
    char_count_dict = {}

    for char in text:
        lowered = char.lower()
        if lowered in char_count_dict:
            char_count_dict[lowered] += 1
        else:
            char_count_dict[lowered] = 1
    return char_count_dict



def sort_dict(dict):
    return dict["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_dict)
    return sorted_list
        

main()
