import random

MINIMUM_SCORE = 0
MAXIMUM_SCORE = 100
EXCELLENT_SCORE = 90
PASSABLE_SCORE = 50
menu = "\nMain Menu:" \
       "\n(G)et a valid score" \
       "\n(P)rint result" \
       "\n(S)how stars " \
       "\n(Q)uit"


def get_score_result(score):
    if score < MINIMUM_SCORE or score > MAXIMUM_SCORE:
        return "Invalid score"
    elif score >= EXCELLENT_SCORE:
        return "Excellent"
    elif score >= PASSABLE_SCORE:
        return "Passable"
    else:
        return "Bad"


def get_valid_score_input():
    user_input = float(input("Enter your score (0-100 inclusive): "))
    while user_input < MINIMUM_SCORE or user_input > MAXIMUM_SCORE:
        print("Invalid number! ")
        user_input = float(input("Enter your score (0-100 inclusive): "))
    return int(user_input)


def print_result(score):
    result = get_score_result(score)
    print(f"Result: {result}")


def show_stars(score):
    stars = "*" * int(round(score))
    print(stars)


def random_score():
    return random.randint(MINIMUM_SCORE, MAXIMUM_SCORE)


def main():
    print("Welcome to the Score Program!")
    score = 0
    print(menu)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score_input()
        elif choice == "P":
            print(score)
            print_result(score)

            random_score_value = random_score()
            result = get_score_result(random_score_value)
            print(f"Random Score: {random_score_value} - Result: {result}")
        elif choice == "S":
            show_stars(score)
        else:
            print("Invalid option. Please choose again.")

        print(menu)
        choice = input(">>> ").upper()


main()

