import os

def get_read_file():
    path_ = input("Path: ")
    if not path_:
        print("Missing path")
    elif not os.path.isfile(path_):
        print("Invalid path")
    else:
        return path_
    return get_read_file()

def get_write_file(path_):
    extension = os.path.splitext(path_)[1]
    if not extension or extension == '.':
        return path_.rstrip('.') + ' (filtered).txt'
    else:
        return path_.replace(extension, ' (filtered).txt')

def get_keywords():
    keywords = input("Keywords: ")
    if keywords:
        return [keyword.strip() for keyword in keywords.split(',')]
    else:
        print("Missing keywords")
        return get_keywords()

def read_lines(path):
    try:
        with open(path) as f:
            return f.readlines()
    except Exception as e:
        print(str(e))

def search_lines(data, keywords):
    if data:
        lines = []
        for number, line in enumerate(data, start=1):
            for keyword in keywords:
                if keyword in line:
                    lines.append(f"{number}: {line}")
                    break
        return lines
    elif isinstance(data, list):
        print("No file data found")

def write_lines(path, lines):
    if lines:
        with open(path, "w") as f:
            f.writelines(lines)
        print("File Generated")
    else:
        print("No keywords found")

def main():
    read_file = get_read_file()             # ex: C:\Users\johndoe\Documents\trace.txt
    write_file = get_write_file(read_file)  # ex: C:\Users\johndoe\Documents\trace (filtered).txt
    keywords = get_keywords()               # ex: COM02 or COM02, Com2
    data = read_lines(read_file)
    lines = search_lines(data, keywords)
    write_lines(write_file, lines)

if __name__ == "__main__":
    main()
