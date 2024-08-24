import argparse

from config.config import config
from cronjob.utils import create_updates_job
from front_end.ft_end_dialogues_choice_logic import *
from back_end.db_interactions import FrontEndDbInteractions
from back_end.init_db import init_db
# from cronjob.cron_price_tracking_and_email_notif import cron_job_run


def run():
    """
       App's central script.
       :return:
    """

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
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--prod", help="run program in production mode", action="store_true")
    parser.add_argument("-c", "--cron", help="run the cron job instead of the main application", action="store_true")
    args = parser.parse_args()

    config.set_runtime_config(is_production_mode=args.prod, is_cron_only=args.cron)

    if config.is_cron_only:
        cron_job_run()

    else:
        run()
