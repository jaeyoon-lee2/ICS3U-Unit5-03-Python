#!/user/bin/env python3

# Created by: Jaeyoon (Jay) Lee
# Created on: Nov 2019
# This program calculate returns the middle percentage mark
#   and takes the level to grade


def calculate_average(first_mark, second_mark, third_mark, fourth_mark):
    # this function calculate the average mark

    # process
    average = (first_mark + second_mark + third_mark + fourth_mark) / 4

    return average


def grade_level(average):
    # this function decides the level of average mark

    # process
    if average >= 95 and average <= 100:
        level = "4+"
    elif average >= 87 and average <= 94:
        level = "4"
    elif average >= 80 and average <= 86:
        level = "4-"
    elif average >= 77 and average <= 79:
        level = "3+"
    elif average >= 73 and average <= 76:
        level = "3"
    elif average >= 70 and average <= 72:
        level = "3-"
    elif average >= 67 and average <= 69:
        level = "2+"
    elif average >= 63 and average <= 66:
        level = "2"
    elif average >= 60 and average <= 62:
        level = "2-"
    elif average >= 57 and average <= 59:
        level = "1+"
    elif average >= 53 and average <= 56:
        level = "1"
    elif average >= 50 and average <= 52:
        level = "1-"
    elif average >= 1 and average <= 49:
        level = "R"
    elif average == 0:
        level = "NE"
    else:
        level = "minus"

    return level


def main():
    # this function gets base and height

    # input
    first_mark = input("Enter your first period mark (integer): ")
    second_mark = input("Enter your second period mark (integer): ")
    third_mark = input("Enter your third period mark (integer): ")
    fourth_mark = input("Enter your fourth period mark (integer): ")

    try:
        first_mark_int = int(first_mark)
        second_mark_int = int(second_mark)
        third_mark_int = int(third_mark)
        fourth_mark_int = int(fourth_mark)

        # call functions
        average = calculate_average(first_mark_int, second_mark_int,
                                    third_mark_int, fourth_mark_int)
        level = grade_level(average)

        # output
        print("Your middle mark is {0}% and level is {1}"
              .format(average, level))
    except Exception:
        print("Theses are not integers")
    finally:
        print("Thanks for playing")


if __name__ == "__main__":
    main()
