num = 456
strnum = '456'
print(f"{str(num) + strnum} is '456' + '456'")
print(f"{int(strnum)+ num} is 456 + 456")
user_input = int(input("enter a number that is larger or equal 10: "))
if user_input > 10:
    print(f"{user_input} is larger than 10. You are correct ")
elif user_input == 10:
    print(f"{user_input} is equal to 10, you are correct ")
elif user_input < 10:
    print(f"{user_input} is smaller than 10, you are wrong! ")
else:
    print(f"Sorry, i don't know what is {user_input} ")
def main(number : int) -> int:
    user_answer_plus3 = user_input + 5
    print(f"{user_answer_plus3} is the number that has plused to 5")
    return user_answer_plus3
main(user_input)