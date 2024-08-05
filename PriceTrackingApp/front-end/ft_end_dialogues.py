from ft_end_dbinteractions import get_username
from ft_end_decorators import menu_decor


username = "Georgia" #Mock name - actual data to be extracted from db with get_username()
@menu_decor
def welcome_back():
    if username == "visitor":
        print("It seems like we have gone ")
    print(f"Welcome back {username}!".center(60))
    print()
