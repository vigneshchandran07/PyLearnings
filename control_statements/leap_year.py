if __name__ == '__main__':
    input_year = int(input("Enter the year"))
    # write code to check if the year is a leap year or not
    if input_year % 4 == 0:
        if input_year % 100 == 0:
            if input_year % 400 == 0:
                print("Leap Year")
            else:
                print("Not a Leap Year")
        else:
            print("Leap Year")
    else:
        print("Not a Leap Year")


