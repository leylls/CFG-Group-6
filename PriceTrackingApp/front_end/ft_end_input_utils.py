from time import sleep
import webbrowser
from front_end.ft_end_ascii_decorators import colours


def clean(string):
    """
    Clean user inputs of extra symbols or spaces, lower cases the answer.
    If given "Yes" or "No" it will refactor it to either "y"/"n" for consistency and easier answer check.
    :param string: str - raw user's input
    :return: cleaned_string as str - trimmed or refactor answer as str
    """
    to_remove = [".", "-", "*", "\\", "/", " ", '"', ",", "!","?",":",";","'","#","@", "[", "]"]
    cleaned_string = string.strip().lower()
    valid_answers_yes = ["yes", "yea", "ye", "yess"]
    valid_answers_no = ["no", "nope", "noo"]

    for char in to_remove:
        cleaned_string = cleaned_string.replace(char, '')

    if cleaned_string in valid_answers_yes:
        return "y"
    elif cleaned_string in valid_answers_no:
        return "n"

    return cleaned_string


def choice_validation(user_input, required_data_type, num_choices=0, exit_option=True):
    """
    Checks that the user input is the correct data type and within the valid choices.
    Use user_input = None to enter the loop without getting Invalid Answer message.
    :param exit_option: True | False - Tells the func if [0] "Exit to Main Menu" is an available option.
    :param user_input: Any - This is the user's answer
    :param required_data_type: str | int  - The required data type for the user input
    :param num_choices: int - The number of choices the user is given - depending on each menu's length.
    :return: True | False - If it's a valid answer or not
    """
    if user_input is None:
        # To enter the loop without raising ValueError i.e. Invalid answer message
        return False
    else:
        try:
            if required_data_type == str:
                user_answer = user_input
                valid_answers = ["n","y"]

            elif required_data_type == int:
                user_answer = int(user_input) # If cannot be turned into and int then it will raise ValueError
                if not exit_option:
                    # To remove "0" as a valid choice if there is not exit [ 0 ] option
                    valid_answers = [num+1 for num in range(num_choices)]
                elif exit_option:
                    valid_answers = [num for num in range(num_choices)]
                if num_choices == 0:
                    # Allows any number >0 to be inserted
                    return True

            if user_answer not in valid_answers:
                raise ValueError

        except ValueError:
            print(f"{colours.error()}Please only type one of the given options!{colours.dialogue()}") # Invalid Answer message
            return False
        except TypeError:
            return False

    return True


def get_user_input(suggestion=None):
    """
    Runs Input method with a suggestion of choice, depending on the data type needed.
    :param suggestion: [str] -> y_n | num | blank
    :return: None
    """
    input_suggestions = {"y_n": f"{colours.main_colour()}  Type either Y or N", "num": f"{colours.main_colour()}   Type a number", None: ""}
    print(input_suggestions[suggestion])
    user_answer = clean(input("->  "))
    print(f"{colours.dialogue()}")
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
        new_answer = None
        is_ready = False
        while not is_ready:
            proceed = None
            while not choice_validation(proceed,str):
                proceed = get_user_input("y_n")
                if proceed == "y":
                    is_ready = True
                else:
                    webbrowser.open_new_tab("https://github.com/evapchiri/evapchiri/blob/main/README.md")
    else:
        print("You can always find the app's instructions".center(60))
        print("in the 'Help' page if needed.\n".center(60))
