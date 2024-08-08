from time import sleep

def app_welcome_ascii():
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
    def deco_wrapper(x,y):
        print(f""" ~~~~~~~~~~~~~~  \\\\  |[*]|   |[*]|   |[*]|  // ~~~~~~~~~~~~~
 |                                                         |""")
        menu_text(x,y)
        print(f""" |                                                          |
 ~~~~~~~~~~~~~~  \\\\   |[*]|   |[*]|   |[*]|  // ~~~~~~~~~~~~~""")
    return deco_wrapper

def menu_option_ascii(opt_num, task_title, func):
    print(f"""  ................  \\      [ {opt_num} ]      //  ...................""")
    print(f"** {task_title} **")
    func()
    print(" " + "."*59)

def new_user_ascii(dialogue):
    def wrapper():
        print(""" ~~~~~~~~~~~~~ \\\\      New User Set up       // ~~~~~~~~~~~~
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~\\\\//~~~~~~~~~~~~~~~~~~~~~~~~~~~
     \n""")
        dialogue()
        print("""\n ~~~~~~~~~~~~~~~~~~~~~~~~~\\\\__//~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n""")
    return wrapper


def goodbye_ascii(goodbye_message):
    def wrapper():
        print("""  ................  \\\\      Bye bye!      //  ................""")
        goodbye_message()
    return wrapper

@goodbye_ascii
def goodbye():
    """
    It prints a nice goodbye message and keeps the app running for a few seconds before exiting.
    :return:
    """
    print("""                 **    Thank you for using    **
                        PriceTrackingApp!
                            *   *   *""")
    sleep(4)
    quit()