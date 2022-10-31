def main():
    print("Enter the name of your file below.")
    myfile = input("> ")
    read_file = open(myfile, 'r').readlines()

    # Initialize counters
    line_count = 1
    column1, column2, column3 = 0, 0, 0

    # print(range(1, len(read_file) - 1))
    # line_count = 1
    # column1 = 0
    # column1 = float(((read_file[line_count]).split())[0]) + column1
    # print(column1)

    for line in range(1, len(read_file) - 1):
        # Get line
        # Split line
        # Get column number
        # # print(line_count)

        column1 = float(((read_file[line_count]).split())[0]) + column1
        column2 = float(((read_file[line_count]).split())[1]) + column2
        column3 = float(((read_file[line_count]).split())[2]) + column3

        line_count = line_count + 1
    
    print("Column             Sum       Average")
    print("------ --------------- -------------")

    column = [column1, column2, column3]
    line_count = line_count - 1
    col_number = 1
    
    for i in column:
        print("%6d %15.2f %13.2f\n" % (col_number, i, i / line_count), end='')
        col_number += 1
    
    # print("%6d %15.2f %13.3f\n" % (1, column1, column1 / line_count), end='')
    # print("%6d %15.2f %13.3f\n" % (2, column2, column2 / line_count), end='')
    # print("%6d %15.2f %13.3f\n" % (3, column3, column3 / line_count), end='')

    # print(f"""
    # File: {myfile}
    # Count: {line_count}
    # Total Column 1: {column1}
    # Average: {column1 / line_count}
    # Total Column 2: {column2}
    # Average: {column2 / line_count}
    # Total Column 3: {column3}
    # Average: {column3 / line_count}
    # """)


main()