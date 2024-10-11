def open_books():
    with open("/home/illeath/workspace/github.com/illeath/bookbot/books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)
def main():
    open_books()

main()