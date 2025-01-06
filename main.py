def count_characters(text):
    counts = {}
    for char in text.lower():
        if char.isalpha():
            if char in counts:
                counts[char] += 1
            else:
                counts[char] = 1
    return counts

def sort_character_counts(char_counts):
    chars_list = []
    for char, count in char_counts.items():
        chars_list.append({"character": char, "count": count})
    
    chars_list.sort(key=lambda x: x["count"], reverse=True)
    return chars_list

def main():
    path = "books/frankenstein.txt"
    with open(path) as f:
        file_contents = f.read()
    
    words = file_contents.split()
    word_count = len(words)
    
    char_counts = count_characters(file_contents)
    sorted_chars = sort_character_counts(char_counts)
    
    print(f"--- Begin report of {path} ---")
    print(f"{word_count} words found in the document\n")
    
    for char_dict in sorted_chars:
        char = char_dict["character"]
        count = char_dict["count"]
        print(f"The '{char}' character was found {count} times")
    
    print("--- End report ---")

if __name__ == "__main__":
    main()