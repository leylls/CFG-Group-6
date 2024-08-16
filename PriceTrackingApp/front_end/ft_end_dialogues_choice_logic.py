from front_end.user_config import current_user
# FRONT END UTILS
from front_end.ft_end_ascii_decorators import *
from front_end.ft_end_input_utils import *
# BACK END IMPLEMENTATION
from front_end.ft_end_backend_interactions import *
from front_end.ft_end_dbinteractions import *


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
    update_user_details(new_user)

    print("""\n
                    > ** ACCOUNT CREATED! ** <\n""")
    print("""               it's time to jump into business!

                       € * £ * ¥ * $""") #TODO perhaps apps name will change?
    return


@menu_option_ascii(1, "Track a new product")
def opt_1_track_new_dialogue():
    """
    Dialogue and logic of the [1] option of Main Menu.
    :return:
    """
    print("""           Please paste the product's Amazon url:\n""")
    print("[or Type 0 to go back to Main Menu]".center(60))
    all_correct = False
    while not all_correct: # To ensure the obtained product details are correct until user is happy
        url = input("""       ->""")

        if url == "0": # Exit function & back to Main Menu
            return False
        print("\n")
        print("""           We are extracting the products details""")
        loading()
        product_data = get_product_data(url)

        print(f"""\n\n        *> Product title:   {product_data['title'][:40]}(...)
    
        *> Current price:   {product_data['currency']}{product_data['price']}\n""")
        print("""                       Are these correct?\n""")
        correct_details = None # To enter loop without error message
        while not choice_validation(correct_details, str):
            # If answer is not either "yes" or "no" (or alternatives) then keep asking the user
            correct_details = get_user_input("y_n")

        if correct_details == "y":
            all_correct = True

        else:
            print("""                      Okay let's try again.
              Please paste the product's Amazon url:""".center(60))

    print("""\n               Would you like to add this product
                     into your email list?\n""")
    notify = get_user_input("y_n")

    if notify == "y": # If "n" then do nothing as default is 'False'
        product_data['email_notif'] = True
        print("""          Please enter the minimum price drop you would 
                      like to be notified for:
    
             (e.g. if you say "5" we will email you when
                 the price has dropped a min of £5)\n""")

        product_threshold = None
        while not choice_validation(product_threshold, int):
            product_threshold = get_user_input("num")
            product_data['prod_threshold'] = int(product_threshold)
            print(f"Great! You will get an email if the price of".center(60))
            print(f"'{product_data['title'][:40]}'".center(60))
            print(f"drops by {product_data['currency']}{product_threshold}".center(60))
    else:
        print("""              If you change your mind, you can set
              email notifications for this product
                on the Email Notifications page""")
        # email_notif is False and prod_threshold is NULL

    # Adding product data/settings to DB
    add_new_tracking(product_data)
    print("""\n               > ** PRODUCT ADDED TO ACCOUNT ** <\n""")
    sleep(2.5)

    ## TRACK ANOTHER ITEM LOOP or return to Main Menu
    print("""                ** * ** * ** * ** * ** * ** * **

                        Choose an option:

                  [ 1 ]  Track another item
                  [ 0 ]  Return to Main Menu""")

    # Needed to enter the choice loop without showing "non-valid answer" message
    final_choice = None
    # Creates a loop until the user_choice is the correct one
    while not choice_validation(final_choice, int, num_choices=2):
        final_choice = get_user_input("num")
    match final_choice:
        case "1": # Enters TRACK NEW loop to keep adding products to track
            return True
        case "0": # Exits & Goes back to Main Menu
            pass
    return False


def print_price_history(produc_id, history_choice):
    match history_choice:
        case "1": # prints 7-day price history chart
            prod_price_history = get_price_history(produc_id, full_history=False)
            print(f"""{data_viz(prod_price_history)}""")
        case "2": # prints full price history chart
            prod_price_history = get_price_history(produc_id, full_history=True)
    return


def opt2_1_price_history():
    print("Please select one from the list:")
    all_products = get_all_tracked_prod()
    print_products(all_products)
    # Needed to enter the choice loop without showing "non-valid answer" message
    user_prod_choice = None
    # Creates a loop until the user_choice is the correct one
    while not choice_validation(user_prod_choice, int, num_choices=len(all_products), exit_option=False):
        user_prod_choice = get_user_input("num")
    selected_product = all_products[user_prod_choice]
    print(f"""            SELECTED:
            **> {selected_product['title'][:40]}""")
    print("""                            Choose an option:

                      [ 1 ]  7-day price history
                      [ 2 ]  All price history""")
    history_choice = None
    # Creates a loop until the user_choice is the correct one
    while not choice_validation(history_choice, int, num_choices=2, exit_option=False):
        history_choice = get_user_input("num")
    print_price_history(selected_product['id'], history_choice)

  #TODO  #####################################


@menu_option_ascii(2, "My tracked products")
def opt_2_tracked_prod_dialogue():
    print("These are your currently tracked products:\n".center(60))
    all_products = get_all_tracked_prod()
    print_products(all_products)
    print("""              ** * ** * ** * ** * ** * ** * **

                 Choose an option:

               [ 1 ]  See a product price history
               [ 2 ]  Delete a product from my list
               [ 0 ]  Return to Main Menu""")
    # Needed to enter the choice loop without showing "non-valid answer" message
    opt_1_choice = None
    repeat_choice = True
    # Creates a loop until the user_choice is the correct one
    while not choice_validation(opt_1_choice, int, num_choices=3):
        opt_1_choice = get_user_input("num")
    match opt_1_choice:
        case "1":
            while repeat_choice:
                repeat_choice = opt2_1_price_history()
        case "2":
            # while repeat_choice:
                #repeat_choice = delete_tracked_product()
            pass
        case "0": # Exits and goes back to Main Menu
            pass
    return False




# opt_2_tracked_prod_dialogue()

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
def get_main_menu_choice():
    """
    Logic behind Main Menu choice selection, and validating user's choice of one of the main menu options, and runs the script of the chosen one.
    :return: None
    """
    #Needed to enter the loop without showing "non-valid answer" message
    user_choice = None
    # Creates a loop until the user_choice is the correct one
    while not choice_validation(user_choice, int, num_choices=6):
        user_choice = get_user_input("num")
    repeat_choice = True
    match user_choice:
        case "1":
            while repeat_choice:
                repeat_choice = opt_1_track_new_dialogue()
        case "2":
            while repeat_choice:
                repeat_choice = opt_2_tracked_prod_dialogue()
        case "3":
            while repeat_choice:
                repeat_choice = opt_3_app_settings_dialoge()
        case "4":
            while repeat_choice:
                repeat_choice = opt_4_email_notifications_dialogue()
        case "5":
            while repeat_choice:
                repeat_choice = opt_5_help_dialogue()
        case "0":
            return True
    return False