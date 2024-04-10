# McDoBot
# Author: Zishen
# 21 Feb 2024



answer = input("would you like fries with your meal? ")
answer_unknown = answer
answer = answer.strip().lower()
if answer == "yes":
    print("Here's your meal with fries! ")
elif answer == "no":
    print("Here's your meal without fries!")
else:
    print(f"Sorry, I don't understand what is {answer_unknown}")