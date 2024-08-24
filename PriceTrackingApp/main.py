import sys

from cronjob.utils import create_updates_job
from front_end.ft_end_dialogues_choice_logic import *
from back_end.db_interactions import FrontEndDbInteractions
from back_end.init_db import init_db
# from cronjob.cron_price_tracking_and_email_notif import cron_job_run


def run(cron_job = False):
    """
       App's central script.
       :return:
    """

    # if cron_job:
    #     cron_job_run()
    #     return


    app_welcome_ascii()
    wants_to_exit = False
    db = FrontEndDbInteractions()

    if not db.db_exists():
        init_db()
        create_updates_job()
        new_user_setup_dialogue()
        sleep(1.5)
        main_menu_text(main_menu_options)

    else:
        welcome_back_text(db.get_username(), main_menu_options)

    while not wants_to_exit:
        wants_to_exit = get_main_menu_choice()
        if wants_to_exit:
            goodbye()
        else:
            main_menu_text(main_menu_options)

    return

if __name__ == "__main__":
    create_updates_job()
    # if len(sys.argv) > 1:                       #check if an argument is passed
    #     argument = sys.argv[1].split('=',1)
    #     if argument[0] == 'cron_job':
    #         run(argument[1])
    # else:
    #     run()
    run()
