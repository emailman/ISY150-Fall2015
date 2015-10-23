__author__ = 'emailman'

done = False
while not done:
    reply = int(input("Enter a positive integer, zero when done: "))
    if reply != 0:
        print("Your input doubled is", reply * 2)
    else:
        done = True
print("All done")