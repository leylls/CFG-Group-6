from time import sleep


def app_welcome_ascii():
    """
    ASCII art to welcome user into the app
    :return:
    """
    print("""                              **
                         ************
                *****************************
============================================================
*          *              WELCOME TO            *          *
*         * *         PRICE TRACKING APP       * *         *
============================================================
                *****************************
                         ************
                              **\n\n""")



def main_menu_ascii(menu_text):
    """
   DECORATOR -  Main Menu ASCII borders - separated from Main Menu options for integration with other menu title text.
    :param menu_text: either "welcome_back" or "Main_menu_text"
    :return:
    """
    def deco_wrapper(*args, **kwargs):
        print(f""" ~~~~~~~~~~~~~~  \\\\  |[*]|   |[*]|   |[*]|  // ~~~~~~~~~~~~~
 |                                                         |""")
        menu_text(*args, **kwargs)
        print(f""" |                                                          |
 ~~~~~~~~~~~~~~  \\\\   |[*]|   |[*]|   |[*]|  // ~~~~~~~~~~~~~""")
    return deco_wrapper


def menu_option_ascii(opt_num, task_title):
    """
    DECORATOR - ASCII border art for EACH Main Menu option.
    :param func: the option logic
    :return:
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"""\n  ................  \\      [ {opt_num} ]      //  ...................""")
            print(f"** {task_title} **\n".center(60))
            func(*args, **kwargs)
            print(" " + "."*59 + "\n")
        return wrapper
    return decorator


def new_user_ascii(dialogue):
    """
    DECORATOR - ASCII border art for New User Set up page.
    :param dialogue:
    :return:
    """
    def wrapper():
        print(""" ~~~~~~~~~~~~~ \\\\      New User Set up       // ~~~~~~~~~~~~
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~\\\\//~~~~~~~~~~~~~~~~~~~~~~~~~~~
     \n""")
        dialogue()
        print("""\n ~~~~~~~~~~~~~~~~~~~~~~~~~\\\\__//~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n""")
    return wrapper


def goodbye():
    """
    Prints a nice goodbye message and keeps the app running for a few seconds before exiting.
    :return:
    """
    print("""  ................  \\\\      Bye bye!      //  ................""")
    print("""                 **    Thank you for using    **
                        PriceTrackingApp!
                            *   *   *""")
    sleep(4)
    quit()


@main_menu_ascii
def welcome_back_text(username, menu_options):
    """
    Welcome CLI text for returning user.
    :param menu_options:
    :return:
    """
    print(f"Welcome back {username}!".center(60))
    print("What would you like".center(60)+"\n"+"to do today?".center(60))
    menu_options()

@main_menu_ascii
def main_menu_text(menu_options):
    """
    Main Menu's CLI text.
    :param menu_options: - Only to be inserted main_menu options
    :return: None
    """
    def wrapper():
        print("""                        \\  MAIN MENU  /

                  What would you like to do?""")
        menu_options()
    return wrapper()


def main_menu_options():
    """
    Main Menu's CLI options.
    :return: None
    """
    print(("""\n               [ 1 ]  Track a new product
               [ 2 ]  My tracked products
               [ 3 ]  My account
               [ 4 ]  Email notifications
               [ 5 ]  Help
               [ 0 ]  Exit""").center(60))
