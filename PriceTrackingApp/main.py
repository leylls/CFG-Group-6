from front_end.ft_end_dialogues_choice_logic import *
from front_end.ft_end_dbinteractions import *
import front_end.user_config as temp_user_config
from back_end.backend_interactions import *
import sys

def run(cron_job = False):
    if cron_job:
        url_list = get_monitored_urls()
        web_scraping = get_ws_results(url_list)
        product_id_and_url = get_product_id_and_urls()
        tuple_results = prepare_results_for_db (web_scraping, product_id_and_url)
        insert_results_db(tuple_results)
        print('done')

        # Check if new prices are below users threshold
        # Send email with all products with prices below threshold
        return
    
    
    """
    App's central script.
    :return:
    """
    app_welcome_ascii()
    wants_to_exit = False
    current_user = temp_user_config.current_user  # For testing logic before DB is fully set up

    if not db_exists():
        new_user_setup_dialogue()
        sleep(1.5)
        main_menu_text(main_menu_options)

    else:
        welcome_back_text(current_user.username, main_menu_options)

    while not wants_to_exit:
        wants_to_exit = get_main_menu_choice()
        if wants_to_exit:
            goodbye()
        else:
            main_menu_text(main_menu_options)
    return

if __name__ == "__main__":
    if len(sys.argv) > 1:                       #check if an argument is passed
        argument = sys.argv[1].split('=',1)
        if argument[0] == 'cron_job':
            run(argument[1])
    else:
        run()