"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
import random


def get_score_result(score):
    if score < 0:
        return "Invalid score"
    elif score > 100:
        return "Invalid score"
    elif score > 90:
        return "Excellent"
    elif score > 50:
        return "Passable"
    else:
        return "Bad"


def main():
    user_score = float(input("Enter your score: "))
    result = get_score_result(user_score)
    print(result)
    random_score = random.randint(0, 100)
    result = get_score_result(random_score)
    print(f"Random Score: {random_score} - Result: {result}")


main()
