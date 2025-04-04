def count_words(text):
    return len(text.split())

def count_characters(text):
    count_by_character = {}

    for character in text:
        lowered_character = character.lower()
        if lowered_character in count_by_character:
            count_by_character[lowered_character] += 1
        else:
            count_by_character[lowered_character] = 1

    return count_by_character

def sort_count_by_characters(count_by_character):
    character_list = []

    for key, value in count_by_character.items():
        character_list.append({"name": key, "count": value})

    character_list.sort(key=sort_on, reverse=True)

    return character_list

def sort_on(dict):
    return dict["count"]
