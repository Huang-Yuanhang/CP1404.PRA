import random

message = """
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

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


def random_score():
    return random.randint(MINIMUM_SCORE, MAXIMUM_SCORE)


def main():
    print(message)
    user_score = float(input("Enter your score: "))
    result = get_score_result(user_score)
    print(result)

    random_score_value = random_score()
    result = get_score_result(random_score_value)
    print(f"Random Score: {random_score_value} - Result: {result}")


main()
