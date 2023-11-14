#!usr/bin/env python3
# Created By: Marli Peters
# Date: Nov. 14, 2023
# This program asks the user to enter a positive number
# and then uses a loop to calculate and display the sum
# of all numbers from 0 to that number.

def main():
    # set loop counter and sum
    loop_counter = 0
    sum = 0

    # get the user number as a string
    user_number_str = str(input("Enter a positive number: "))
    print("")

    try:
        # try typecasting number
        user_number_int = int(user_number_str)

    except:
        # catch exceptions
        print("Please enter a valid integer.")

    else:
        #start loop
        while loop_counter <= user_number_int:
            sum = sum + loop_counter
            # display numbers through loop
            print("Tracking {0} times through loop.".format(loop_counter))
            loop_counter = loop_counter + 1

        # display results of calculation
        print("")
        print("The sum of the numbers from 0 to {} is: {}.".format(user_number_int, sum))

if __name__ == "__main__":
    main()
