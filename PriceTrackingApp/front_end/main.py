from ft_end_dialogues import *
from ft_end_utils import *
from ft_end_dbinteractions import *

def run():
    if db_exists():
        new_user_dialogue()
        main_menu_text(main_menu_options)

    elif not db_exists():
        welcome_back_text(main_menu_options)

    user_choice = None

    #TODO main_menu_choice()
    """
    TO ENCAPSULATE ALL BELOW IN main_menu_choice() for reusability 
    """

    #Creates a loop until the user_choice is the correct one
    while not choice_validation(user_choice, int, num_choices=6):
        user_choice = get_user_input("num")

    match user_choice:
        case "1":
            opt_1_track_new()
        case "2":
            opt_2_tracked_prod()
        case "3":
            opt_3_app_settings()
        case "4":
            opt_4_email_notifications()
        case "5":
            opt_5_help()
        case "0":
            goodbye()


if __name__ == "__main__":
    # run()



