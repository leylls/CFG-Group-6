from time import sleep
import webbrowser

def clean(string):
    """
    Clean user inputs of extra symbols or spaces, lower cases the answer.
    If given "Yes" or "No" it will refactor it to either "y"/"n" for consistency and easier answer check.
    :param string: str - raw user's input
    :return: cleaned_string as str - trimmed or refactor answer as str
    """
    to_remove = [".", "-", "*", "\\", "/", " ", '"', ",", "!","?",":",";","'","#","@"]
    cleaned_string = string.strip().lower()

    for char in to_remove:
        cleaned_string = cleaned_string.replace(char, '')

    if cleaned_string == "yes":
        return "y"
    elif cleaned_string == "no":
        return "n"

    return cleaned_string


def choice_validation(user_input, data_type, num_choices=0):
    """
    Checks that the user input is the correct data type and within the valid choices.
    Use user_input = None to enter the loop without getting Invalid Answer message.
    :param user_input: this is the user's answer
    :param data_type: str | int  - the expected data type of the
    :param num_choices: int - the number of choices the user is given - depending on menu length.
    :return: True | False
    """
    if user_input is None: #To enter the loop without raising ValueError i.e. Invalid answer message
        return False
    else:
        try:
            if data_type == str:
                user_answer = user_input
                valid_answers = ["n","y"]
                if user_answer not in valid_answers:
                    raise ValueError

            elif data_type == int:
                user_answer = int(user_input) # If cannot be turned into and int then it will raise ValueError
                valid_answers = [num for num in range(num_choices)]
                if user_answer not in valid_answers:
                    raise ValueError
            else:
                raise TypeError("Incorrect datatype argument given")
                # This is for apps development, if Exception is raised then it means the data_type parameter is wrong

        except ValueError:
            print("Please only type one of the given options!") # Invalid Answer message
            return False
        except TypeError:
            return False

    return True


def get_user_input(suggestion=None):
    """
    Runs Input method with a suggestion of choice, depending on the data type needed.
    :param suggestion: [str] y_n | num | blank
    :return: None
    """
    #TODO function documentation in other functions
    input_suggestions = {"y_n": "  Type either Y or N", "num": "   Type a number", None: ""}
    print(input_suggestions[suggestion])
    user_answer = clean(input("->  "))
    return user_answer


def loading():
    """
    Prints out a loading message to look like the app has a process running.
    :return:
    """
    print("Please wait".center(60))
    print(" ".center(25), end=' ')
    for x in list("." * 4):
        print(x, end=' ')
        sleep(0.8)


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
        print("Very well, please provide an email:".center(60))
        is_correct = False
        while not is_correct:
            user_email = input("->   ")
            print("Is this email correct?".center(60))
            print(f"{user_email}".center(60))
            answer = get_user_input("y_n")
            if answer == "y":
                is_correct = True
            else:
                print("Okay let's try again".center(60))
    elif email_pref == "n":
        print("""\n                   If you change your mind,\n        you can always set up email notifications
         later on the [4]Email notifications page.\n""")

    return {"email_pref": email_pref, "user_email": user_email}

def get_app_instructions():
    answer = None
    while not choice_validation(answer, str):
        # While the answer cannot be validated, then keep asking the user until valid answer
        answer = get_user_input("y_n")
    if answer == "y":
        webbrowser.open_new_tab("https://github.com/evapchiri/evapchiri/blob/main/README.md")
        print("""
                               Now that you know everything,""")
        print("do you want to continue?".center(60))
        print("""                    [ Y ] Yes, I am ready!
                    [ N ] No, I need to see that again.""")
        proceed = None
        while not choice_validation(proceed,str):
            proceed = get_user_input("y_n")
        if proceed == "y":
            pass
        else:
            webbrowser.open_new_tab("https://github.com/evapchiri/evapchiri/blob/main/README.md")
            proceed = get_user_input("y_n")
    else:
        print("Brave!\nYou can always find the app's instructions\nin the 'Help' page if needed.".center(60))

def main_menu_choice():
    """
    Logic behind asking, and validating user's choice of one of the main menu options, and runs the script of the chosen one.
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