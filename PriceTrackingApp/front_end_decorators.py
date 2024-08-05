
def app_welcome_decor():
    def printout():
        print("\n")
        print(" "*30 + "**")
        print(" " * 25 + "*"*12)
        print(" " * 16 + "*" * 28)
        print("="*60)
        print("*" + " " * 10 + "*" + " "*14 + "WELCOME TO" + " "*12 + "*" + " "*10 + "*")
        print("*" + " " * 9 + "* *" + " " * 9 + "PRICE TRACKING APP" + " " * 7 + "* *" + " " * 9 + "*")
        print("=" * 60)
        print(" " * 16 + "*" * 28)
        print(" " * 25 + "*" * 12)
        print(" " * 30 + "**")
        print("\n\n\n")

    return printout()


def menu_decor(func):
    def wrapper():
        print(" " + "~"*14 + " " + "\\"*2 + "  " + "|[*]|" + "  "+ "|[*]|" + "  " + "|[*]|" + "  " + "//" + " "+ "~"*13)
        print(" "+"|"+" "*55+"|")
        func()
        print(" " + "|" + " " * 55 + "|")
        print(" " + "~"*14 + " " + "\\"*2 + "  " + "|[*]|" + "  "+ "|[*]|" + "  " + "|[*]|" + "  " +"//" + " "+ "~"*13)
    return wrapper
