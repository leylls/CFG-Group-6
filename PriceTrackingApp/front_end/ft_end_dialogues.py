from ft_end_ascii_decorators import *
from ft_end_input_utils import *
from user_config import User

# Mock name - real data
# current_user = "Georgia"


@new_user_ascii
def new_user_setup_dialogue():
    """
    Full CLI dialogue to set up the main details of the new user (user_name + email_pref + user_email).
    :return: None
    """
    print("""            I see that you are new around here.
          How about we set up a few things first?

              For example, what is your name?\n""")
    user_name = input("->  ").title()
    print(f"Great! Nice to meet you {user_name}.\n".center(60))
    sleep(2)
    print("""                Our app has been created to 
         help you track the price of any product 
         and assess when is the best time to shop!\n""")
    sleep(5)
    # APP INSTRUCTIONS #
    print("""       Do you want to know how to use this app?
            [ Y ] Yes please!
            [ N ] No thank you, I already know how it works.""")
    get_app_instructions()
    # EMAIL SECTION #
    print("""** @ **\n""".center(60))
    print("""         We can notify you by email of any price drop
                within the range of your choice.

                    Does this interest you?\n""")
    print("""                        [ Y ] Yes please
            [ N ] No thank you, I will check manually.\n""")
    user_email_settings = set_up_email_notifications()
    print("""** @ **\n""".center(60))
    sleep(4)
    print("We are now creating your account".center(60))
    new_user = User(user_name, user_email_settings["email_pref"], user_email=user_email_settings["user_email"])
    loading()


    print("""\n
                    ** Acount created! **""")
    print("""               it's time to jump into business!

                       € * £ * ¥ * $""") #TODO perhaps apps name will change?
    return new_user


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
    print("""                        \\  MAIN MENU  /

                  What would you like to do?""")
    menu_options()

def main_menu_options():
    """
    Main Menu's CLI options.
    :return: None
    """
    print(("""\n               [ 1 ]  Track a new product
               [ 2 ]  My tracked products
               [ 3 ]  App settings
               [ 4 ]  Email notifications
               [ 5 ]  Help
               [ 0 ]  Exit""").center(60))

#
# @menu_option_ascii(1, "Track a new product")
# def opt_1_track_new_dialogue():
#     print(""" """) #TODO Set up options for this task
#     pass
#
# @menu_option_ascii(2, "My tracked products")
# def opt_2_tracked_prod_dialogue():
#     print(""" """) #TODO Set up options for this task
#     pass
#
# @menu_option_ascii(3, "App settings")
# def opt_3_app_settings_dialoge():
#     print(""" """) #TODO Set up options for this task
#     pass
#
# @menu_option_ascii(4, "Email notifications")
# def opt_4_email_notifications_dialogue():
#     print(""" """) #TODO Set up options for this task
#     pass
#
# @menu_option_ascii(5, "My tracked products")
# def opt_5_help_dialogue():
#     print(""" """) #TODO Set up options for this task
#     pass
#
#
# @goodbye_ascii
# def goodbye():
#     """
#     It prints a nice goodbye message and keeps the app running for a few seconds before exiting.
#     :return:
#     """
#     print("""                 **    Thank you for using    **
#                         PriceTrackingApp!
#                             *   *   *""")
#     sleep(4)
#     quit()
