

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


def menu_decor(func):
    def wrapper():
        print(f""" ~~~~~~~~~~~~~~  \\\\  |[*]|   |[*]|   |[*]|  // ~~~~~~~~~~~~~
 |                                                         |""")
        func()
        print(f""" |                                                          |
 ~~~~~~~~~~~~~~  \\\\   |[*]|   |[*]|   |[*]|  // ~~~~~~~~~~~~~""")
    return wrapper

def menu_option_decor(opt_num, opt_task, func):
    print(f"""  ................  \\      [ {opt_num} ]      //  ...................""")
    print(f"** {opt_task} **")
    func()
    print(" " + "."*59)