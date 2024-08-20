from front_end.ft_end_dialogues_choice_logic import *
from front_end.ft_end_dbinteractions import *
from back_end.init_db import init_db
import front_end.user_config as temp_user_config

def run():
    """
    App's central script.
    :return:
    """
    wants_to_exit = False
    current_user = temp_user_config.current_user  # For testing logic before DB is fully set up

    if not db_exists():
        init_db()
        new_user_setup_dialogue()
        sleep(1.5)
        main_menu_text(main_menu_options)

    else:
        welcome_back_text(current_user.username, main_menu_options)

    while not wants_to_exit:
        wants_to_exit = get_main_menu_choice()
        if wants_to_exit:
            goodbye()
        else:
            main_menu_text(main_menu_options)
    return

if __name__ == "__main__":
    app_welcome_ascii()
    run()



