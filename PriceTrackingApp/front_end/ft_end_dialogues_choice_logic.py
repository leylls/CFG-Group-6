# FRONT END UTILS
from front_end.ft_end_ascii_prints import *
from front_end.ft_end_input_utils import *
# BACK END IMPLEMENTATION
from front_end.ft_end_backend_interactions import *
from front_end.ft_end_dbinteractions import *


def set_up_email_notifications():
    """
    ** This will need proper docs*** lol
    :return:
    """
    email_pref = None  # To enter the first loop without getting error message for invalid choice
    user_email = None  # Unless email_pref is "y" then will change to user's email
    while not choice_validation(email_pref, str):
        # While the answer cannot be validated, then keep asking the user until valid answer
        email_pref = get_user_input("y_n")
    if email_pref == "y":
        print("We thought it would.".center(60))
        is_correct = False
        while not is_correct:
            colours.question("Please provide us with your email:".center(60))
            user_email = input(f"{colours.main_colour()}\n->  ")
            print("\n")
            colours.question("Is this email correct?".center(60))
            print(f"{user_email}\n".center(60))
            answer = get_user_input("y_n")
            if answer == "y":
                is_correct = True
            else:
                print("Okay let's try again\n".center(60))
    elif email_pref == "n":
        print("""\n                   If you change your mind,\n        you can always set up email notifications
           later on the "Email notifications" page.\n""")

    return {"email_pref": email_pref, "user_email": user_email}


def get_app_instructions():
    """
    Logic to open PriceTrackingApp's README from Github and ensure user feels ready to use the app.
    :return:
    """
    answer = None
    while not choice_validation(answer, str):
        # While the answer cannot be validated, then keep asking the user until valid answer
        answer = get_user_input("y_n")
    if answer == "y":
        webbrowser.open_new_tab("https://github.com/evapchiri/evapchiri/blob/main/README.md")
        sleep(2)
        colours.question("""                Now that you know everything,
                do you want to continue?""")
        print("""            [ Y ] Yes, I am ready!
            [ N ] No, I need to see that again.\n""")
        is_ready = False
        while not is_ready:
            proceed = None
            while not choice_validation(proceed,str):
                proceed = get_user_input("y_n")
                if proceed == "y":
                    is_ready = True
                else:
                    webbrowser.open_new_tab("https://github.com/evapchiri/evapchiri/blob/main/README.md")
                    #TODO change url with actual app's README url when finished
    else:
        print("You can always find the app's instructions".center(60))
        print("in the 'Help' page if needed.\n".center(60))


@new_user_ascii
def new_user_setup_dialogue():
    """
    Full CLI dialogue to set up the main details of the new user (user_name + email_pref + user_email).
    :return: None
    """
    colours.question("Hello there! 👋".center(60))
    print("""            I see that you are new around here.
          How about we set up a few things first?\n""")

    colours.question("For example, what is your name?\n".center(60))
    user_name = input(f"{colours.main_colour()}->  ").title()
    print("\n")
    colours.question(f"Great! Nice to meet you {user_name}.\n".center(60))
    sleep(2)
    print("""               Our app has been created to 
     help you track the price of any AMAZON product 
    and help you assess when is the best time to shop!\n""")
    sleep(5)
    # APP INSTRUCTIONS #
    colours.question("Do you want to know how to use this app?".center(60))
    print("""            [ Y ] Yes, please!
            [ N ] No thank you, I already know how it works.\n""")
    get_app_instructions()
    sleep(3)
    # EMAIL SECTION #
    colours.question("""** @ **\n""".center(60))
    sleep(1)
    print("""         We can notify you by email of any price drop
              within the range of your choice.\n""")
    sleep(3.5)
    colours.question("Does this interest you?".center(60))
    print("""            [ Y ] Yes, it does.
            [ N ] No thank you, I will check the app manually.\n""")
    user_email_settings = set_up_email_notifications()
    colours.question("""** @ **\n""".center(60))
    sleep(4)
    print("We are now creating your account".center(60))
    loading()

    new_user = {'username': f'{user_name}',
                'email_pref': f'{user_email_settings["email_pref"]}',
                'user_email': f'{user_email_settings["user_email"]}'}
    update_user_details(new_user)
    print("\n")
    colours.notification("*> ACCOUNT CREATED! <*\n".center(60))
    sleep(2.5)
    colours.question("""               It's time to jump into business!

                       € * £ * ¥ * $""")
    sleep(2.5)
    return


@menu_option_ascii(1, "TRACK A NEW PRODUCT")
def opt_1_track_new_dialogue():
    """
    Dialogue and logic of the [1] option of Main Menu.
    :return:
    """
    colours.question("""           Please paste the product's Amazon url:""")
    print(f"  (or Type 0 to go back to Main Menu)\n".center(60))
    all_correct = False
    while not all_correct: # To ensure the obtained product details are correct until user is happy
        try:
            url = input(f"""{colours.main_colour()}->  """)
            print(f"{colours.dialogue()}")

            if url == "0": # Exit function & back to Main Menu
                return False
            print("""           We are extracting the products details""")
            loading()
            product_data = get_product_data(url)
            print("\n\n")
            colours.question("----------------- ** ----------------- ".center(60))
            print(f"""\n  *> Product title:   {product_data['title'][:32]}(...)
        
  *> Current price:   {product_data['currency']}{product_data['price']}\n""")
            colours.question("----------------- ** ----------------- ".center(60))
            colours.question("""                    Are these correct?\n""")
            correct_details = None # To enter loop without error message
            while not choice_validation(correct_details, str):
                # If answer is not either "yes" or "no" (or alternatives) then keep asking the user
                correct_details = get_user_input("y_n")

            if correct_details == "y":
                all_correct = True

            else:
                print("""                   Okay let's try again.""")
                colours.question("""           Please paste the product's Amazon url:""")

        except IndexError:
            # Reusable for either when URL invalid or Error when retrieving data
            error_printout("""        We could not extract the product information.
                      Please try again.""")
            colours.question("""           Please paste the product's Amazon url:""")

    colours.question("""\n            Would you like to add this product
                  into your email list?\n""")
    notify = None
    while not choice_validation(notify, str):
        notify = get_user_input("y_n")

    if notify == "y":
        product_data['email_notif'] = True
        colours.question("""       Please enter the minimum price drop you would 
                like to be notified for:""")
    
        print("""        (e.g. if you say "5" we will email you when
            the price has dropped a min of £5)\n""")

        product_threshold = None
        while not choice_validation(product_threshold, int, exit_option=False):
            product_threshold = get_user_input("num")
            product_data['price_threshold'] = int(product_threshold)
            print(f"Great! You will get an email if the price of".center(60))
            print(f"'{product_data['title'][:40]}'".center(60))
            print(f"drops by {product_data['currency']}{product_threshold}".center(60))
    else:
        # Product's email_notif is False and prod_threshold is 0
        print("""              If you change your mind, you can set
              email notifications for this product
                on the Email Notifications page""")


    # Adding product data/settings to DB
    add_new_tracking(product_data)
    colours.notification("""\n             > ** PRODUCT ADDED TO ACCOUNT ** <\n""")
    sleep(2.5)

    ## TRACK ANOTHER ITEM LOOP or return to Main Menu
    print("""              ** * ** * ** * ** * ** * ** * **""")
    colours.question("Choose an option:".center(60))
    print("""               [ 1 ]  Track another item
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
    """
    Prints out a graph and the history log of the given product(by ID) and the history length (7-day/Full)
    :param produc_id: int
    :param history_choice: str:  1 | 2
    :return:
    """
    match history_choice:
        case "1": # prints 7-day price history chart
            prod_price_history = get_price_history(produc_id, full_history=False)
            colours.notification("*> 7 DAY PRICE HISTORY <*".center(60))
            print(f"""{data_viz(prod_price_history)}""")
        case "2": # prints full price history chart
            prod_price_history = get_price_history(produc_id, full_history=True)
            colours.notification("*> FULL PRICE HISTORY <*".center(60))
            print(f"""{data_viz(prod_price_history)}""")
    return


def opt2_1_price_history():
    colours.question("Please select one from the list:".center(60))
    all_products = get_all_tracked_prod()
    print_products(all_products, "num")
    # Needed to enter the choice loop without showing "non-valid answer" message
    user_prod_choice = None
    # Creates a loop until the user_choice is the correct one
    while not choice_validation(user_prod_choice, int, num_choices=len(all_products), exit_option=False):
        user_prod_choice = get_user_input("num")

    selected_product = all_products[int(user_prod_choice)-1]
    colours.notification(f"""            SELECTED:
            **> {selected_product['title'][:40]}\n""")

    print("""              ** * ** * ** * ** * ** * ** * **""")
    colours.question("Choose an option:".center(60))
    print("""               [ 1 ]  7-day price history
               [ 2 ]  Full price history""")

    history_choice = None
    # Creates a loop until the user_choice is the correct one
    while not choice_validation(history_choice, int, num_choices=2, exit_option=False):
        history_choice = get_user_input("num")
    print_price_history(int(selected_product['id']), history_choice)
    match history_choice:
        case "1":  # User originally chose 7-day - show alternative opt (Full price) again
            print("\n")
            print("""              ** * ** * ** * ** * ** * ** * **""")
            colours.question("Choose an option:".center(60))
            print("""               [ 1 ]  See product Full price history
               [ 0 ]  Return to Main Menu\n""")
        case "2":  # User originally chose Full price history - show alternative opt (7-day) again
            print("\n")
            print("""              ** * ** * ** * ** * ** * ** * **""")
            colours.question("Choose an option:".center(60))
            print("""               [ 1 ]  See product 7-day price history
               [ 0 ]  Return to Main Menu\n""")

    final_choice = None
    while not choice_validation(final_choice, int, num_choices=2, exit_option=True):
        final_choice = get_user_input("num")

    match final_choice:
        case "1":
            if history_choice == "1":
                # User originally chose 7-day price history - so Full price history will be now shown
                print_price_history(int(selected_product['id']), "2")
            elif history_choice == "2":
                # User originally chose Full-day price history - so 7-day price history will be now shown
                print_price_history(int(selected_product['id']), "1")
        case "0":
            return False

    print("""              ** * ** * ** * ** * ** * ** * **""")
    input(f"{colours.main_colour()}\nPress Enter to return to Main Menu\n  ->  ")
    return False


def delete_tracked_product():
    correct = False
    while not correct:
        colours.question("Please select one from the list:".center(60))
        all_products = get_all_tracked_prod()
        print_products(all_products, "num")
        # Needed to enter the choice loop without showing "non-valid answer" message
        user_prod_choice = None
        # Creates a loop until the user_choice is the correct one
        while not choice_validation(user_prod_choice, int, num_choices=len(all_products), exit_option=False):
            user_prod_choice = get_user_input("num")

        selected_product = all_products[int(user_prod_choice) - 1]
        colours.notification(f"""            SELECTED:
            **> {selected_product['title'][:40]}\n""")

        print("""              ** * ** * ** * ** * ** * ** * **\n""")
        colours.question("Are you sure you want to delete this product?:\n".center(60))
        user_answer = None
        while not choice_validation(user_answer, str):
            user_answer = get_user_input("y_n")
        if user_answer == "y":
            stop_tracking(int(selected_product['id']))
            correct = True
            colours.notification(f"*> {selected_product['title'][:40]} HAS BEEN DELETED <*\n".center(60))
            sleep(2)
            colours.question("Do you want to delete any other product?\n".center(60))
            repeat = None
            while not choice_validation(repeat, str):
                repeat = get_user_input("y_n")
            if repeat == "y":
                return True
            else:
                print("We are taking you now to the Main Menu\n".center(60))
                sleep(2)
        else:
            pass

    return False


@menu_option_ascii(2, "MY TRACKED PRODUCTS")
def opt_2_tracked_prod_dialogue():
    print("These are your currently tracked products:\n".center(60))
    all_products = get_all_tracked_prod()
    print_products(all_products, "star")

    print("""              ** * ** * ** * ** * ** * ** * **""")
    colours.question("Choose an option:".center(60))
    print("""               [ 1 ]  See a product price history
               [ 2 ]  Delete a product from my list
               [ 0 ]  Return to Main Menu\n""")

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
            while repeat_choice:
                repeat_choice = delete_tracked_product()
        case "0": # Exits and goes back to Main Menu
            pass
    return False

def opt_3_1_updt_details(user_details):
    colours.question("What would you like to update?".center(60))
    print("""               [ 1 ]  USERNAME
               [ 2 ]  EMAIL\n""")
    detail_choice = None
    while not choice_validation(detail_choice, int, num_choices=2, exit_option=False):
        detail_choice = get_user_input("num")
    is_correct = False
    match detail_choice:
        case "1":
            while not is_correct:
                colours.question(f"Please provide your new USERNAME:".center(60))
                new_username = input(f"{colours.main_colour()}->  ").title()
                print("\n")
                colours.question("Is this correct?".center(60))
                print(f"{new_username}\n".center(60))
                answer = get_user_input("y_n")
                if answer == "y":
                    is_correct = True
                    user_details['username'] = new_username
                    update_user_details(user_details)
                    colours.notification("*> YOUR USERNAME HAS BEEN UPDATED <*\n".center(60))
                else:
                    print("Okay let's try again\n".center(60))
        case "2":
            while not is_correct:
                colours.question(f"Please provide your new EMAIL:".center(60))
                new_email = input(f"{colours.main_colour()}->  ")
                print("\n")
                colours.question("Is this correct?".center(60))
                print(f"{new_email}\n".center(60))
                answer = get_user_input("y_n")
                if answer == "y":
                    is_correct = True
                    user_details['user_email'] = new_email
                    update_user_details(user_details)
                    colours.notification("*> YOUR EMAIL HAS BEEN UPDATED <*\n".center(60))
                else:
                    print("Okay let's try again\n".center(60))

    ## UPDATE ANOTHER DETAIL LOOP or return to Main Menu
    print("""              ** * ** * ** * ** * ** * ** * **""")
    colours.question("Choose an option:".center(60))
    print("""               [ 1 ]  Update something else
               [ 0 ]  Return to Main Menu""")

    # Needed to enter the choice loop without showing "non-valid answer" message
    final_choice = None
    # Creates a loop until the user_choice is the correct one
    while not choice_validation(final_choice, int, num_choices=2):
        final_choice = get_user_input("num")
    match final_choice:
        case "1":  # Enters loop to update another user detail
            print("These are your current details:\n".center(60))
            current_user_details = get_user_details()
            print(f"""{colours.main_colour()}        *> USERNAME: {user_details['username']}
        *> EMAIL: {user_details['user_email']}\n{colours.dialogue()}""")
            return True
        case "0":  # Exits & Goes back to Main Menu
            pass

    return False


@menu_option_ascii(3, "MY ACCOUNT DETAILS")
def opt_3_acc_details_dialogue():

    print("These are your current details:\n".center(60))
    current_user_details = get_user_details()
    print(f"""{colours.main_colour()}        *> USERNAME: {current_user_details['username']}
        *> EMAIL: {current_user_details['user_email']}\n""")

    print(f"""{colours.dialogue()}              ** * ** * ** * ** * ** * ** * **""")
    colours.question("Choose an option:".center(60))
    print("""               [ 1 ]  Update details
               [ 0 ]  Return to Main Menu\n""")
    user_answer = None
    while not choice_validation(user_answer, int, num_choices=2):
        user_answer = get_user_input("num")
    repeat_choice = True
    match user_answer:
        case "1":
            while repeat_choice:
                repeat_choice = opt_3_1_updt_details(current_user_details)
        case "0":
            pass

    return False




#
# @menu_option_ascii(4, "EMAIL NOTIFICATIONS")
# def opt_4_email_notifications_dialogue():
#     print(""" """) #TODO Set up options for this task
#     pass
#

@menu_option_ascii(5, "HELP")
def opt_5_help_dialogue():
    print("Need some help figuring out how to use the app?\n".center(60))
    print(f"{colours.main_colour()}Our README📄 is packed with all the".center(60))
    print("information you’ll need.\n".center(60))
    sleep(4.5)
    colours.question("Would you like to open it in your browser?\n".center(60))
    user_answer = None
    while not choice_validation(user_answer, str):
        user_answer = get_user_input("y_n")

    if user_answer == "y":
        webbrowser.open_new_tab("https://github.com/evapchiri/evapchiri/blob/main/README.md")
        sleep(2)
        print(f"""              ** * ** * ** * ** * ** * ** * **""")
        colours.question("Choose an option:".center(60))
        print("""               [ 1 ]  Open README📄 again
               [ 0 ]  Return to Main Menu\n""")

        # Making a little loop to keep opening README if needed
        is_ready = False
        while not is_ready:
            final_choice = None
            while not choice_validation(final_choice, int, num_choices=2):
                final_choice = get_user_input("num")
                if final_choice == "0":
                    is_ready = True
                else:
                    webbrowser.open_new_tab("https://github.com/evapchiri/evapchiri/blob/main/README.md")
                    # TODO change url with actual app's README url when finished
    else:
        print("No worries!".center(60))
        print("The README📄 will always be available if you need it.\n".center(60))
        sleep(2)
        print("We are now taking you back to the Main Menu\n".center(60))
        sleep(2.5)
    return False


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
                repeat_choice = opt_3_acc_details_dialogue()
        case "4":
            while repeat_choice:
                repeat_choice = opt_4_email_notifications_dialogue()
        case "5":
            while repeat_choice:
                repeat_choice = opt_5_help_dialogue()
        case "0":
            return True
    return False
