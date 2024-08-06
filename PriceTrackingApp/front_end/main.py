# from ft_end_dialogues import *
from ft_end_utils import *
# from ft_end_dbinteractions import *
# def run():
#     if db_exists():
#         new_user_dialogue()
#         main_menu_text(main_menu_options)
#
#     elif not db_exists():
#         welcome_back_text(main_menu_options)
    # user_choice = choice_validation()
    # match choice_validation(clean(get_user_input("num"))):
    #     case "1":


if __name__ == "__main__":
    # run()
    answer = choice_validation(get_user_input("num"))
    print(answer)



