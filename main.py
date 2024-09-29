def main():
    filename = "books/frankenstein.txt"
    with open(filename) as f:
        file_contents = f.read()
        word_count = count_words(file_contents)
        count_of_each_character = count_each_character(file_contents.lower())
        count_sorted = convert_and_sort(count_of_each_character)
        print_report(filename, word_count, count_sorted)

def count_words(book):
    words = book.split()
    return len(words)

def count_each_character(book):
    count_dict = {}
    for character in book:
        if character not in count_dict:
            count_dict[character] = 1
        else:
            count_dict[character] += 1
    
    return count_dict

def convert_and_sort(count_dict):
    count_list = []
    for character in count_dict:
        if character.isalpha():
            count_list.append({"character": character, "count": count_dict[character]})
    
    count_list.sort(reverse=True, key=sort_on)
    return count_list

def sort_on(dict):
    return dict["count"]

def print_report(filename, word_count, sorted_character_counts):
    print(f"--- Begin report of {filename} ---")
    print(f"{word_count} words found in the document")
    print("")

    for character in sorted_character_counts:
        print(f"The {character['character']} character was found {character['count']} times")

    print("--- End report ---")


main()