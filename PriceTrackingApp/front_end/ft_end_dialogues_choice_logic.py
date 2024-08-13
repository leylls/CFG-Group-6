import user_config
# FRONT END UTILS
from ft_end_ascii_decorators import *
from ft_end_input_utils import *
# BACK END IMPLEMENTATION
from ft_end_backend_interactions import *
from ft_end_dbinteractions import *


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
    loading()

    #TODO Write new user details into DB
    new_user = {'username': f'{user_name}',
                'email_pref': f'{user_email_settings["email_pref"]}',
                'user_email': f'{user_email_settings["user_email"]}'}

    print("""\n
                    > ** ACCOUNT CREATED! ** <\n""")
    print("""               it's time to jump into business!

                       € * £ * ¥ * $""") #TODO perhaps apps name will change?
    return


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


@menu_option_ascii(1, "Track new product")
def opt_1_track_new_dialogue():
    print("""           Please paste the product's Amazon url:\n""")
    print("[or Type 0 to go back to Main Menu]".center(60))
    is_correct = False
    while not is_correct: # To ensure the obtained product details are correct until user is happy
        url = get_user_input()

        if url == "0": # Exit back to Main Menu # TODO to refactor and avoid recursion
            main_menu_text(main_menu_options)
            main_menu_choice()

        product_data = get_product_data(url)
        print("""           We are extracting the products details""")
        loading()
        print(f"""\n\n        *> Product title:   {product_data['title']}
    
        *> Current price:   {product_data['currency']}{product_data['price']}\n""")
        print("""                       Are these correct?\n""")
        correct_details = get_user_input("y_n")

        if correct_details == "y":
            is_correct = True

        else:
            print("""                      Okay let's try again.
              Please paste the product's Amazon url:""".center(60))

    print("""\n               Would you like to add this product
                     into your email list?\n""")
    notify = get_user_input("y_n")

    if notify == "y": # If "n" then do nothing as default is 'False'
        product_data['email_notif'] = True

    else:
        print("""              If you change your mind, you can set
              email notifications for this product
                on the Email Notifications page""")

    add_new_tracking(product_data)
    print("""\n               > ** PRODUCT ADDED TO ACCOUNT ** <\n""")
    sleep(2.5)
    print("""                ** * ** * ** * ** * ** * ** * **

                        Choose an option:

                  [ 1 ]  Track another item
                  [ 0 ]  Exit to Main Menu""")

    # Needed to enter the loop without showing "non-valid answer" message
    final_choice = None
    # Creates a loop until the user_choice is the correct one
    while not choice_validation(final_choice, int, num_choices=2):
        final_choice = get_user_input("num")
    match final_choice: # TODO Refactor to avoid recursion / memory leak
        case "1": # Goes back to
            opt_1_track_new_dialogue()
        case "0":
            main_menu_text(main_menu_options)
            main_menu_choice()


# opt_1_track_new_dialogue()


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
def main_menu_choice():
    """
    Logic behind Main Menu choice selection, and validating user's choice of one of the main menu options, and runs the script of the chosen one.
    :return: None
    """
    #Needed to enter the loop without showing "non-valid answer" message
    user_choice = None
    # Creates a loop until the user_choice is the correct one
    while not choice_validation(user_choice, int, num_choices=6):
        user_choice = get_user_input("num")

    match user_choice:
        case "1":
            opt_1_track_new_dialogue()
        case "2":
            opt_2_tracked_prod_dialogue()
        case "3":
            opt_3_app_settings_dialoge()
        case "4":
            opt_4_email_notifications_dialogue()
        case "5":
            opt_5_help_dialogue()
        case "0":
            goodbye()
