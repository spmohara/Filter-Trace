import os

def get_read_file():
    path = input("Path: ")
    if os.path.splitext(path)[1]:
        return path
    else:
        print("Missing or invalid path")
        return get_read_file()

def get_keywords():
    keywords = input("Keywords: ")
    if keywords:
        return [keyword.strip() for keyword in keywords.split(',')]
    else:
        print("Missing keywords")
        return get_keywords()

def get_write_file():
    return read_file.replace('.txt', ' (filtered).txt')

def read_lines():
    with open(read_file) as f:
        return f.readlines()

def write_lines(lines):
    if lines:
        with open(write_file, "w") as f:
            f.write(lines)
        print("File generated")
    else:
        print("No keywords found")
        search_lines(get_keywords())

def search_lines(keywords):
    lines = ""
    for number, line in enumerate(read_lines(), 1):
        for keyword in keywords:
            if keyword in line:
                lines += "{}: {}".format(number, line)
                break
    write_lines(lines)

if __name__ == "__main__":
    read_file = get_read_file()     # ex: C:\Users\johndoe\Documents\myfile.txt
    keywords = get_keywords()       # ex: COM02 or COM02, Com2
    write_file = get_write_file()   # ex: C:\Users\johndoe\Documents\myfile (filtered).txt
    search_lines(keywords)
