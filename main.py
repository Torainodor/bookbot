def get_text(file):
    with open(file) as f:
        file_content = f.read()
    return file_content

def count_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    letter_count = {}
    for char in text:
        char = char.lower()
        if char not in letter_count:
            letter_count[char] = 1
        else:
            letter_count[char] += 1

    return letter_count #{"letter": int}

def sort_letters(dict):
    pretty_letters = []
    for key in dict:
        if str(key).isalpha():
            temp = {"letter": key, "num": dict[key]}
            pretty_letters.append(temp)
    pretty_letters.sort(reverse=True, key=sort_on)
    return pretty_letters

def sort_on(dict):
    return dict["num"]

def main ():
    file_name = "books/frankenstein.txt"
    text = get_text(file_name)
    words = count_words(text)
    print(f"There are {words} in the {file_name}")
    letters_count = count_letters(text)
    pretty_letters = sort_letters(letters_count)
    for letter in pretty_letters:
        print(f"The '{letter["letter"]}' character was found {letter["num"]} times")

main()
