# 2a. Write the file mode that will be used for opening the following files. Also, write the
# Python statements to open the following files: a text file “example.txt” in both read and
# write mode
# a binary file “bfile.dat” in write mode
# a text file “try.txt” in append and read mode
# a binary file “btry.dat” in read only mode.


with open("example.txt", "r+") as example_file:
    # perform operations on example_file
    pass  # replace with actual operations

with open("bfile.dat", "wb") as bfile:
    # perform operations on bfile
    pass  # replace with actual operations

with open("try.txt", "a+") as try_file:
    # perform operations on try_file
    pass  # replace with actual operations

with open("btry.dat", "rb") as btry_file:
    # perform operations on btry_file
    pass  # replace with actual operations
