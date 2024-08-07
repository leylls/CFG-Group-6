from front_end.ft_end_dbinteractions import *
from front_end.ft_end_choice_logic import *


def run():
    if db_exists():
        new_user_setup_dialogue()
        main_menu_text(main_menu_options)

    elif not db_exists():
        welcome_back_text(main_menu_options)

    main_menu_choice()


if __name__ == "__main__":
    run()



