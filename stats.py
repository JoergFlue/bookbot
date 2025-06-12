def get_num_words(text):
    """
    Returns the number of words in the given text.
    """
    return len(text.split())

def get_character_dictionary(text):
    """
    Returns a dictionary with the number of occurrences of each character in the text.
    """
    char_dict = {}
    for c in text:
        if not c.isalpha():
            continue
        cl = c.lower()
        if cl in char_dict:
            char_dict[cl] += 1
        else:
            char_dict[cl] = 1
    return char_dict

def sort_on(d):
    return d["num"]

def chars_dict_to_sorted_list(char_dict):
    """
    Converts a dictionary of characters and their counts to a sorted list of dictionaries.
    """
    char_dict_list = [{"char": c, "num":n} for c, n in char_dict.items()]
    char_dict_list.sort(reverse=True, key=sort_on)
    return char_dict_list