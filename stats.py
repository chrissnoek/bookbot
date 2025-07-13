def count_words(text):
    num_words = len(text.split())
    print(f"Found {num_words} total words")

def count_chars(text):
    char_dict = {}
    all_chars = list(text.lower())
    for i in range(0, len(all_chars)):
        letter = all_chars[i]

        if letter in char_dict:
            char_dict[letter] = char_dict[letter] + 1
        else:
            char_dict[letter] = 1
    return char_dict

def sort_chars(char_dict):
    list = []
    for char, count in char_dict.items():
        if char.isalpha():
            list.append({'char': char, 'count': count})
    def sort_on(items):
        return items["count"]
    list.sort(reverse=True, key=sort_on)
    for i in range(0, len(list)):
        print(f"{list[i]['char']}: {list[i]['count']}")
        