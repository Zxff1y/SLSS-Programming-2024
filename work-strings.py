# Work strings
# Author: Zishen Gong
# 21 Feb 2024

def greet():
    print("Hello! Welcome to the conversation.")

def ask_name():
    name = input("What's your name? ")
    return name

def ask_questions(name):
    print(f"Nice to meet you, {name}!")
    print("Let's ask you a few questions:")
    answer1 = input("What is your favorite colour? ")
    answer2 = input("What is your favorite food? ")
    answer3 = input("Where is your dream vacation destination? ")
    return answer1, answer2, answer3

def respond(name, answer):
    print(f"Great answers, {name}!")
    print(f"So, your favorite colour is {answer[0]}, favorite food is {answer[1]},  and dream vacation destination is {answer[2]}.")

def say_goodbye(name):
    print(f"Goodbye, {name}! Have a great day!")

def main():
    greet()
    user_name = ask_name()
    answers = ask_questions(user_name)
    respond(user_name, answers)
    say_goodbye(user_name)

if __name__ == "__main__":
    main()


