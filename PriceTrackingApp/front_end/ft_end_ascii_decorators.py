

def app_welcome_ascii():
    def printout():
        print("""\n                              **
                         ************
                *****************************
============================================================
*          *              WELCOME TO            *          *
*         * *         PRICE TRACKING APP       * *         *
============================================================
                *****************************
                         ************
                              ** \n\n\n""")

    return printout()


def main_menu_ascii(func):
    def wrapper():
        print(f""" ~~~~~~~~~~~~~~  \\\\  |[*]|   |[*]|   |[*]|  // ~~~~~~~~~~~~~
 |                                                         |""")
        func()
        print(f""" |                                                          |
 ~~~~~~~~~~~~~~  \\\\   |[*]|   |[*]|   |[*]|  // ~~~~~~~~~~~~~""")
    return wrapper

def menu_option_ascii(opt_num, task_title, func):
    print(f"""  ................  \\      [ {opt_num} ]      //  ...................""")
    print(f"** {task_title} **")
    func()
    print(" " + "."*59)

def new_user_ascii(dialogue):
    print(""" ~~~~~ \\\\             New User Set up             // ~~~~~
 ~~~~~~~~~~~~~~~~~~~~~~~~~~\\\\//~~~~~~~~~~~~~~~~~~~~~~~~~~~\n""")
    dialogue()
    print("""\n ~~~~~~~~~~~~~~~~~~~~~~~~~\\\\__//~~~~~~~~~~~~~~~~~~~~~~~~~~""")


def goodbye_ascii(goodbye_message):
    print("""  ................  \\\\      Bye bye!      //  ................""")
    goodbye_message()