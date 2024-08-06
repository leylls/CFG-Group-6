def clean(string):
    """
    Clean user inputs of extra symbols or spaces, lower cases the answer.
    If given "Yes" or "No" it will refactor it to either "y"/"n" for consistency and easier answer check.
    :param string: str - raw user's input
    :return: cleaned_string as str - trimmed or refactor answer as str
    """
    to_remove = [".", "-", "*", "\\", "/", " ", '"', ","]
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
    :param user_input: this is the user's answer
    :param data_type: str | int  - the expected data type of the
    :param num_choices: int - the number of choices the user is given - depending on menu length.
    :return: True | False
    """
    if user_input == None:
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
            print("Please only type one of the given options!")
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

def goodbye(): #TODO
    """
    It prints a nice goodbye message and keeps the app running for a few seconds before exiting.
    :return:
    """
