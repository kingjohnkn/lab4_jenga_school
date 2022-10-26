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


numbers()