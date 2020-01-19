import oopexample

maths = oopexample.NumChange()

def main():
    num = float(input("Please enter a number: "))
    added = maths.addfive(num)
    multip = maths.multiply(added)
    print("the manipulated value is ", multip)


main()