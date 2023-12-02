def main():
    book_path = "books/frankenstein.txt"
    print(f"--- Begin report of {book_path} --- ")
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")
    char_counts = count_chars_in_text(text)
    display_char_count(char_counts)

def display_char_count(char_counts):
    for char, count in sort_by_value(char_counts):
        if char.isalpha():
            print(f"The '{char}' character was found {count} times")

def sort_by_value(dict):
    return sorted(dict.items(), key=lambda x: x[1], reverse=True)

def get_num_words(text):
    words = text.split()
    return len(words)

def count_chars_in_text(text):
    char_counts = {}
    for char in text:
        lower_char = char.lower()
        if lower_char in char_counts:
            char_counts[lower_char] += 1
        else:
            char_counts[lower_char] = 1
    return char_counts

def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
