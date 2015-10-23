__author__ = 'emailman'

done = False
while not done:
    try:
        reply1, reply2 = input('Enter two integers, two zeros when done: ').split()
        int1, int2 = [int(reply1), int(reply2)]
        if int1 == 0 and int2 ==0:
            done = True
        else:
            print("The sum of your inputs =", int1 + int2)
    except:
        print("You did not enter two integers")

print("All done")
