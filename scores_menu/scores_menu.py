MINIMUM_SCORE = 0
MAXIMUM_SCORE = 100
EXCELLENT_SCORE = 90
PASSABLE_SCORE = 50


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
    while True:
        user_input = input("Enter your score (0-100 inclusive): ")
        if user_input.isdigit():
            user_score = float(user_input)
            if MINIMUM_SCORE <= user_score <= MAXIMUM_SCORE:
                return user_score
            else:
                print(f"Score should be between {MINIMUM_SCORE} and {MAXIMUM_SCORE}. Please try again.")
        else:
            print("Invalid input. Please enter a valid number.")


def print_result(score):
    result = get_score_result(score)
    print(f"Result: {result}")


def show_stars(score):
    stars = "*" * int(score)
    print(stars)


def get_user_choice():
    return input(">>> ").upper()


def handle_user_choice(choice, score):
    if score is None:
        print("Please enter a valid score first.")
        return None

    if choice == "G":
        score = get_valid_score_input()
        return score
    elif choice == "P":
        print_result(score)
    elif choice == "S":
        show_stars(score)
    elif choice == "Q":
        print("Thank you for using the Score Program. Goodbye!")
        exit()
    else:
        print("Invalid option. Please choose again.")
    return score


def main():
    score = None  # Initialize the score to None
    print("Welcome to the Score Program!")

    while True:
        print("\nMain Menu:")
        print("(G)et a valid score")
        print("(P)rint result")
        print("(S)how stars")
        print("(Q)uit")

        choice = get_user_choice()
        score = handle_user_choice(choice, score)


main()

