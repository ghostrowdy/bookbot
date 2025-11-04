def display_word_count(file):
    with open(file) as f:
        word_list = f.read().split()
        print(f'Found {len(word_list)} total words')

def count_characters(file):
    with open(file) as f:
        text_string = f.read().lower()
    character_dict = {}
    for character in text_string:
        if character not in character_dict:
            character_dict[character] = 1
        elif character == ' ':
            continue
        else:
            character_dict[character] += 1
    return character_dict

def sort_character_dictionary(dict):
    list = []
    for i in dict:
        list.append({'char': i, 'num': dict[i]})
    list.sort(reverse=True, key=sort_on)
    return list

def sort_on(items):
    return items['num']
