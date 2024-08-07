from front_end.ft_end_dialogues import *

current_user = None

def run(user):
    if user is None:
        current_user = new_user_setup_dialogue()
        sleep(4.5)
        main_menu_text(main_menu_options)

    else:
        welcome_back_text(user.username, main_menu_options)

    main_menu_choice()


if __name__ == "__main__":
    app_welcome_ascii()
    run(current_user)



