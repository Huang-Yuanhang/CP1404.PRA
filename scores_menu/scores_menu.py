import score


def get_valid_scores():
    while True:
        try:
            scores = float(input("Enter your score (0-100): "))
            if 0 <= scores <= 100:
                return scores
            else:
                print("Score must be between 0 and 100. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid score (0-100).")


def print_stars(scores):
    print("Stars: " + "*" * int(scores))


def main():
    user_score = None
    while True:
        print("\n====== Main Menu ======")
        print("(G)et valid score")
        print("(P)rint result")
        print("(S)how stars")
        print("(Q)uit")

        choice = input("Please select a menu option (enter the first letter): ").strip().lower()

        if choice == 'g':
            user_score = get_valid_scores()
        elif choice == 'p':
            try:
                if user_score is not None:
                    result = score.get_score_result(user_score)
                    print("Your Result:", result)
                else:
                    print("You haven't entered a valid score yet. Please choose (G)et valid score to enter your score.")
            except NameError:
                print("You haven't entered a valid score yet. Please choose (G)et valid score to enter your score.")
        elif choice == 's':
            try:
                if user_score is not None:
                    print_stars(user_score)
                else:
                    print("You haven't entered a valid score yet. Please choose (G)et valid score to enter your score.")
            except NameError:
                print("You haven't entered a valid score yet. Please choose (G)et valid score to enter your score.")
        elif choice == 'q':
            print("Thank you for using the program. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")


main()
