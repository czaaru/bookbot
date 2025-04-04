from stats import count_words
from stats import count_characters
from stats import sort_count_by_characters
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    text = get_book_text(path)
    text_count = count_words(text)
    character_count = count_characters(text)
    sorted_character_count = sort_count_by_characters(character_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {text_count} total words")
    print("--------- Character Count -------")

    for character in sorted_character_count:
        if character["name"].isalpha():
            print(f"{character['name']}: {character['count']}")

    print("============= END ===============")

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

main()
