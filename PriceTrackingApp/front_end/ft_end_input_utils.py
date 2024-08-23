from time import sleep
import webbrowser
from front_end.ft_end_ascii_prints import colours


def clean(string):
    """
    Clean user inputs of extra symbols or spaces, lower cases the answer.
    If given "Yes" or "No" it will refactor it to either "y"/"n" for consistency and easier answer check.
    :param string: str - raw user's input
    :return: cleaned_string as str - trimmed or refactor answer as str
    """

    try:
        float(string)
        return string
    except ValueError:
        pass

    to_remove = [".", "-", "*", "\\", "/", " ", '"', ",", "!","?",":",";","'","#","@", "[", "]"]
    valid_answers_yes = ["yes", "yea", "yeah", "ye", "yess"]
    valid_answers_no = ["no", "nope", "noo"]

    cleaned_string = string.strip().lower()
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
    :param required_data_type: str | int | float  - The required data type for the user input
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

            elif required_data_type == float:
                float(user_input)
                return True

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


def is_valid_email(email):
    if "@" in email:
        username, domain = email.split("@", 1)
        if len(username) > 0 and "." in domain and len(domain.split(".")[-1]) > 1:
            return True
    raise ValueError(f"The email address '{email}' is not valid.")