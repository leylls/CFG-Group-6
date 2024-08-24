import datetime
import os.path
import sys

from cronjob.task_scheduler import create_task


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
    directory_for_project = os.getcwd()
    cronjob_directory = os.path.join(directory_for_project, "cronjob")
    job_wrapper_vb_script_path = os.path.join(cronjob_directory, "job_wrapper.vbs")

    write_job_config_files(directory_for_project, cronjob_directory)

    # return create_task("trackmazon_update_task", ("MINUTE", "1"), os.path.abspath(os.path.join("cronjob","job.bat")))
    return create_task("trackmazon_update_task", ("MINUTE", "1"), job_wrapper_vb_script_path)

def write_job_config_files(directory_for_project, cronjob_directory):

    batch_file_path = os.path.join(cronjob_directory, "job.bat")
    job_wrapper_vb_script_path = os.path.join(cronjob_directory, "job_wrapper.vbs")

    replacements = {
        "PROJECT_DIRECTORY": directory_for_project,
        "BATCH_FILE_LOCATION": batch_file_path,
        "EXECUTE_JOB_COMMAND": f"{sys.executable} {os.path.join(directory_for_project, "cron_main.py")}"
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
