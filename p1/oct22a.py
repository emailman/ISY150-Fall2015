__author__ = 'emailman'

done = False

while not done:
    try:
        reply = int(input("Enter a positive integer, zero when done: "))
        if reply != 0:
            print("Your input doubled is", reply * 2)
        else:
            done = True
    except:
        print("You did not enter an integer")

print("All done")
