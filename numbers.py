import math

def numbers():
    print("Starting the Process")
    myfile = open("numbers.txt", 'w')
    myfile.write("Numbers Squared Sq. Root\n")
    myfile.write("------- ------- --------\n")

    for i in range(1, 101):
        myfile.write("%6d %7d %7.3f\n" % (i, i*i, math.sqrt(i)))
        
    myfile.close()
    print("Finished writing the File")

def read_numbers():
    print()
    infile = open("numbers.txt", 'r')
    # allstr = infile.read()
    # print(allstr)

    for i in range(10):
        s = infile.readline()
        # remove trailing newline character
        print(s[:-1])

    infile.close()

def read_numbers2():
    infile = open("numbers.txt", 'r')

    # lines = infile.readlines()
    # --- Print the lines in the file in a list ---
    # print(lines)

    # --- Read the file as a list of lines ---
    # for s in lines:
    #     print(s[:-1])

    # --- Use the file as if it is a list of lines ---
    for s in infile:
        print(s[:-1])
        
    infile.close()


numbers()
read_numbers()
read_numbers2()