__author__ = 'emailman'


def main():
    # Open a file for reading
    data_file = open('data.txt', 'r')

    # Read all the lines from the file
    lines = data_file.readlines()

    # Print the file's contents
    for line in lines:
        # There will be an extra blank line if \n if not stripped from the end
        print(line.rstrip('\n'))

    # Close the file
    data_file.close()


main()
