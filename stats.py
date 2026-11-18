# Support file for main containing functions for getting stats from book strings.

def count_words(string):
    num_of_words = len(string.split())
    return num_of_words

def count_characters(string):
    #lower all the characters to avoid duplicates:
    string = string.lower()
    character_dictionary = {}
    for character in string:
        if character in character_dictionary:
            character_dictionary[character] += 1
        else:
            character_dictionary[character] = 1
    return character_dictionary

def sort_on(items):
    return items["num"]

def sort_characters(dictionary):
    # First we need to convert out dictionary into a list of dictionaries with the char , num attributes
    list_of_dictionaries = []
    for char, num in dictionary.items():
        list_of_dictionaries.append({"char": char, "num": num})

    # Sort based on the "num" attribute
    list_of_dictionaries.sort(reverse=True, key=sort_on)
    return list_of_dictionaries