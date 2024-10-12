def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    chars_list = transform_dict_to_list(chars_dict)
    print("report start")
    print(f"{num_words} words found in the document")
    print()
    for item in chars_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' has been found {item['num']} times")
    print("end of report")


def sort_on(d) :
    return d["num"]

def transform_dict_to_list(num_chars_dict):
    report_list = []
    for ch in num_chars_dict:
        report_list.append({"char": ch, "num" :num_chars_dict[ch]})
    report_list.sort(reverse = True, key = sort_on)
    return report_list

def get_num_words(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()