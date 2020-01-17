
def main():
    loopnum = int(input("Enter the number of loops you would like to recursively repeat: "))
    counter = 1
    recurr(loopnum, counter)


def recurr(loopnum, counter):
    if loopnum > 0:
        print("The loop iteration number is: ", counter)
        recurr(loopnum -1, counter + 1)
    else:
        print("the loop has ended")


main()