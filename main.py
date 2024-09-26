def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_chars = get_num_chars(text)
    print("--- Begin report of {0} ---".format(book_path))
    print('{0} words found in the document\n'.format(num_words))
    for(k,v) in num_chars.items():
        print("The '{0}' character was found {1} times".format(k,v))

def get_num_chars(text):
    from collections import OrderedDict
    chars = {e:text.lower().count(e) for e in set(char_set())}
    ordered_chars = OrderedDict(sorted(chars.items(), key=lambda kv: kv[1], reverse=True))
    return ordered_chars

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def char_set():
    return {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 
            'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}

main()