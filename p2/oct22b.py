__author__ = 'emailman'

done = False
while not done:
    try:
        reply1, reply2 = input('Enter two integers, zero when done: ').split()
        int1, int2 = [int(reply1), int(reply2)]
        if int1 != 0:
            print("The sum of your inputs = ", int1 + int2)
        else:
            done = True
    except:
        print("You did not enter a integer")
print("All done")
