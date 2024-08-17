from time import sleep


class Colours:
    def dialogue(self):
        return "\33[0m"
    def error(self):
        return "\33[91m"
    def notification(self, text:str):
        return print(f"\33[92m{text}{colours.dialogue()}")
    def main_colour(self):
        return "\33[93m"
    def question(self, text:str):
        return print(f"{colours.main_colour()}{text}{colours.dialogue()}")
    # def main_colour(self):
    #     return "\33[92m"


colours = Colours()


def app_welcome_ascii():
    """
    ASCII art to welcome user into the app
    :return:
    """
    print(f"""{colours.main_colour()}                              **
                         ************
                *****************************
============================================================
*          *              WELCOME TO            *          *
*         * *         PRICE TRACKING APP       * *         *
============================================================
                *****************************
                         ************
                              **\n\n""")
    print(f"{colours.dialogue()}")


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
            true_false = func(*args, **kwargs)
            print(" " + "."*59 + "\n\n")
            return true_false
        return wrapper
    return decorator


def new_user_ascii(dialogue):
    """
    DECORATOR - ASCII border art for New User Set up page.
    :param dialogue:
    :return:
    """
    def wrapper():
        print(f""" ~~~~~~~~~~~~~ \\\\      New User Set up       // ~~~~~~~~~~~~
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~\\\\//~~~~~~~~~~~~~~~~~~~~~~~~~~~
     \n""")
        dialogue()
        print(f"""\n ~~~~~~~~~~~~~~~~~~~~~~~~~\\\\__//~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n""")
    return wrapper


def goodbye():
    """
    Prints a nice goodbye message and keeps the app running for a few seconds before exiting.
    :return:
    """
    print(f"""{colours.main_colour()}  ................  \\\\      Bye bye!      //  ................""")
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
    colours.question(f"""  Welcome back {username}!\n""".center(60))
    colours.question("   What would you like".center(60)+"\n"+"  to do today?".center(60))
    menu_options()

@main_menu_ascii
def main_menu_text(menu_options):
    """
    Main Menu's CLI text.
    :param menu_options: - Only to be inserted main_menu options
    :return: None
    """
    def wrapper():
        print("\\  MAIN MENU  /\n".center(60))
        colours.question("What would you like to do?".center(60))
        menu_options()
    return wrapper()


def main_menu_options():
    """
    Main Menu's CLI options.
    :return: None
    """
    print(f"""\n               [ 1 ]  Track a new product
               [ 2 ]  My tracked products
               [ 3 ]  My account
               [ 4 ]  Email notifications
               [ 5 ]  Help
               [ 0 ]  Exit""".center(60))


def print_products(product_list, index_type, collapsed=False):
    """
    Prints out the title (if not collapsed: and price) of a given list of products.
    :param type: str : 'num' | 'star'
    :param product_list: [list]
    :param collapsed: i.e. toggle print products price
    :return:
    """
    i = 0
    match index_type:
        case "num":
            index = [str(num+1) for num in range(len(product_list))]
        case "star":
            index = ["*"]*len(product_list)
    if not collapsed:
        for product in product_list:
            print(f"""      [ {index[i]} ]  {product['title'][:40]}(...)
                   *> Current price: {product['currency']}{product['price']}\n""")
            i+=1
    else:
        for product in product_list:
            print(f"""      [ {index[i]} ]  {product['title'][:40]}(...)""")
            i+=1
    return

def error_printout(text):
    """
    Prints out special ascii to decorate the app's error messages.
    :param text: Particular error message to display
    :return:
    """
    print(f"{colours.error()}\n")
    print("⚠️".center(60))
    print(f"{text}\n")