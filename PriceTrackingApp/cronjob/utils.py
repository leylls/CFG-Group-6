import datetime
import os.path
import sys

from cronjob.task_scheduler import create_task


def is_bundled_application():
    """
    Function to determine during runtime if the app is running as an executable built by PyInstaller or through python.
    PyInstaller provide this code in their docs:
    https://pyinstaller.org/en/stable/runtime-information.html#run-time-information
    :return: Boolean - whether the app is running as an executable bundle or just with python
    """
    return getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS')


def track_sent_mail(sent_mail):
    """
    It writes the HTML from the email it would be sent by API into a "log" within cronjob/job_logs - so we don't use up the API credits.
    :param sent_mail:
    :return:
    """
    current_timestamp = datetime.datetime.now().isoformat()[:-7].replace(':', '-')

    log_file = open(os.path.join("cronjob", "job_logs", f"job_result_{current_timestamp}.html"), 'w')
    log_file.write(sent_mail['HTMLPart'])
    log_file.close()


def create_updates_job():
    """
    Interacts with Window's Task Scheduler to the cron-job task
    :return:
    """
    # current_dir = os.path.dirname(os.path.abspath(__file__))
    directory_for_project = os.getcwd()
    cronjob_directory = os.path.dirname(os.path.abspath(__file__)) #os.path.join(directory_for_project, "_internal", "cronjob") if is_bundled_application() else os.path.join(directory_for_project, "cronjob")
    job_wrapper_vb_script_path = os.path.join(cronjob_directory, "job_wrapper.vbs")

    write_job_config_files(directory_for_project, cronjob_directory)

    # FOR TESTING
    # return create_task("trackmazon_update_task", ("MINUTE", "1"), os.path.abspath(os.path.join("cronjob","job.bat")))
    # return create_task("trackmazon_update_task", ("MINUTE", "1"), f"{job_wrapper_vb_script_path}")

    return create_task("trackmazon_update_task", ("DAILY", "1"), f"{job_wrapper_vb_script_path}")


def write_job_config_files(directory_for_project, cronjob_directory):
    """
    It swaps replacements's keys with its values in the cron bat file.
    :param directory_for_project:
    :param cronjob_directory:
    :return:
    """
    batch_file_path = os.path.join(cronjob_directory, "job.bat")
    job_wrapper_vb_script_path = os.path.join(cronjob_directory, "job_wrapper.vbs")

    replacements = {
        "PROJECT_DIRECTORY": directory_for_project,
        "BATCH_FILE_LOCATION": f"{batch_file_path}",
        "EXECUTE_JOB_COMMAND": f"{sys.executable} --cron"
    } if is_bundled_application() else {
        "PROJECT_DIRECTORY": directory_for_project,
        "BATCH_FILE_LOCATION": f"{batch_file_path}",
        "EXECUTE_JOB_COMMAND": f"{sys.executable} --cron"
    }

    for filepath in [batch_file_path, job_wrapper_vb_script_path]:
        file_lines = []
        with open(filepath, 'r') as file:
            for line in file:
                for (key, value) in replacements.items():
                    line = line.replace(key, value)
                file_lines.append(line)
        with open(filepath, 'w') as file:
            file.writelines(file_lines)
