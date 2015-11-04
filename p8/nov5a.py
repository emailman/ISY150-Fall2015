__author__ = 'emailman'


def main():
    # Open a file for writing
    data_file = open('data.txt', 'w')
    for i in range(10):
        for j in range(20):
            data_file.write(str(i * j) + '\t')
        # New line after the end of the inner loop
        data_file.write('\n')

    # Close the file
    data_file.close()
main()
