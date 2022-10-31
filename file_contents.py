def main():
    print("What's your file name?")
    myfile = input("> ")
    print("Processing ... \n")
    read_file = open(myfile, 'r').readlines()
    # print(read_file)

    line_count = 0
    word_count = 0
    char_count = 0

    for line in read_file:
        sentence = read_file[line_count]
        word_count = len(sentence.split()) + word_count
        char_count = len(read_file[line_count]) + char_count
        line_count = line_count + 1

    print(f"Your file, {myfile}, has {line_count} lines, {word_count} words, and {char_count} characters.")
    
    # print(f"""{myfile}
    # Lines: {line_count}
    # Words: {word_count}
    # Charactes: {char_count}
    # """)
    

main()
