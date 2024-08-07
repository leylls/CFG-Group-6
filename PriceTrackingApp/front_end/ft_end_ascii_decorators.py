

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
    def deco_wrapper(menu_options):
        print(f""" ~~~~~~~~~~~~~~  \\\\  |[*]|   |[*]|   |[*]|  // ~~~~~~~~~~~~~
 |                                                         |""")
        menu_text(menu_options)
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
    print("""  ................  \\\\      Bye bye!      //  ................""")
    goodbye_message()