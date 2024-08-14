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


def choice_validation(user_input, data_type, num_choices=0, exit_option=True):
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
                if not exit_option:
                    # To remove "0" as a valid choice if there is not exit [ 0 ] option
                    valid_answers = valid_answers[1:]
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
                print("Okay let's try again\n".center(60))
    elif email_pref == "n":
        print("""\n                   If you change your mind,\n        you can always set up email notifications
         later on the [4]Email notifications page.\n""")

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
        print("""
                Now that you know everything,""")
        print("do you want to continue?".center(60))
        print("""            [ Y ] Yes, I am ready!
            [ N ] No, I need to see that again.""")
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
        print("""\n      You can always find the app's instructions\n             in the 'Help' page if needed.""".center(60))
