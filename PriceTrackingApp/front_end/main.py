from front_end.ft_end_dialogues_choice_logic import *
from front_end.ft_end_dbinteractions import *

def run():
    """
    App's central script.
    :return:
    """
    current_user = user_config.current_user  # For testing logic before DB is fully set up
    if not db_exists():
        new_user_setup_dialogue()
        sleep(4.5)
        main_menu_text(main_menu_options)

    else:
        welcome_back_text(current_user.username, main_menu_options)

    main_menu_choice()


if __name__ == "__main__":
    app_welcome_ascii()
    run()



