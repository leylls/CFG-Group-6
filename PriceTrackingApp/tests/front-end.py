from front_end.ft_end_input_utils import *
# from front_end.ft_end_dbinteractions import *
# from front_end.ft_end_dialogues import *

# answer = choice_validation(get_user_input("num"), int, 5) #User can only choose 0-4
# user_choice = get_user_input("num")
# print(user_choice)
# print(f"Is it valid? {choice_validation(user_choice, int,num_choices=6)}")
user_choice = None
while not choice_validation(user_choice, int, num_choices=6):
    user_choice = get_user_input("num")

print("We made it out woooooo")
