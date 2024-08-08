from front_end.ft_end_dialogues import *
from front_end.ft_end_choice_logic import *


def run():
    current_user = user_config.current_user
    if current_user is None:
        new_user_setup_dialogue()
        sleep(4.5)
        main_menu_text(main_menu_options)

    else:
        welcome_back_text(current_user.username, main_menu_options)

    main_menu_choice()


if __name__ == "__main__":
    app_welcome_ascii()
    run()



