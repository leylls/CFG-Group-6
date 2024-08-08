from ft_end_input_utils import *
from ft_end_ascii_decorators import *

# def main_menu_choice():
#     """
#     Logic behind asking, and validating user's choice of one of the main menu options, and runs the script of the chosen one.
#     :return: None
#     """
#     #Needed to enter the loop without showing "non-valid answer" message
#     user_choice = None
#     # Creates a loop until the user_choice is the correct one
#     while not choice_validation(user_choice, int, num_choices=6):
#         user_choice = get_user_input("num")
#
#     match user_choice:
#         case "1":
#             opt_1_track_new_dialogue()
#         case "2":
#             opt_2_tracked_prod_dialogue()
#         case "3":
#             opt_3_app_settings_dialoge()
#         case "4":
#             opt_4_email_notifications_dialogue()
#         case "5":
#             opt_5_help_dialogue()
#         case "0":
#             goodbye()
